ApplicationKernel.namespace('Service');

/**
 * Service is responsible of new user environment initialization
 * e.g. when user registers and has  no invitation new workspace and default vault is created
 *
 */
Service.NewUserInit = Ember.Object.extend({
    /**
     * @DI service:auth
     */
    auth: null,

    /**
     * @DI service:invitations
     */
    invitations: null,


    /**
     * @DI service:router
     */
    router: null,


    /**
     * Creates route transition function after initialization
     * @param {Vaultier.dal.model.Node}node
     */
    createTransitionFunction: function (node) {
        var router = this.get('router');
        return function () {
            router.transitionTo('Document.list', node);
        }
    },


    /**
     * if condition met function creates workspace and vault for new user
     *
     * returns success promise with desired transition function,
     * which executed transition router to page desired by initialization
     *
     * resolve({
     *          transitionAfterRegister: function,
     *          createdWorkspace: Vaultier.dal.model.Workspace
     *          createdVault: Vaultier.dal.model.Vault
     * })
     *
     * @return {Ember.RSVP.Promise}
     */
    initializeUser: function () {
        var auth = this.get('auth');
        var invitations = this.get('invitations')

        if (!auth.get('isAuthenticated')) {
            throw new Error('User is not authenticated')
        }

        // in case there are invitations in session do nothing
        if (invitations.hasInvitationsInSession()) {
            return Ember.RSVP.resolve(this.createTransitionFunction());
        }

        // prepare variables and copywriting
        var helpers = Utils.HandlebarsHelpers.create();
        var nickname = helpers.ucfirst(auth.get('user.nickname'));


        // prepare objects to save
        var node = new Vaultier.dal.model.Node();
        node.setProperties({
            name: 'Default folder',
            type: Vaultier.dal.model.Node.proto().types.FOLDER.value,
            color: 'blue'


        });

        var notifyError = function (error) {
                    $.notify('Ooops! Something went wrong.', 'error');
                    throw error;
                };

        // saves the object
        return node
            .saveRecord()
            .then(function (response) {
                Utils.Logger.log.debug(response);
                this.get('tree').addRootNode(node, response.id);
            }.bind(this))
            .catch(notifyError)
            .then(function () {
                return new Ember.RSVP.Promise(function (resolve) {
                    resolve({
                        transitionAfterRegister: this.createTransitionFunction(node),
                        /**
                         * Stores default node if created by newuserinitservice
                         */
                        node: node,
                        role_node: this.get('store').find('Role', { node: node.get('id') }),
                        role_parent_node: this.get('store').find('Role', { parent_node: node.get('id') })
                    })
                }.bind(this));
            }.bind(this))
    }

})
;
