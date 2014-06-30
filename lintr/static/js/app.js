angular.module('app', ['ngRoute', 'app.controllers', 'app.directives', 'app.services']).
        config(['$routeProvider', '$locationProvider', 'Routes', function($routeProvider, $locationProvider, Routes) {
            $locationProvider.html5Mode(false);
            $locationProvider.hashPrefix('');
            $routeProvider
                .when(Routes.main, {
                    controller: 'main', templateUrl: 'mainTemplate'
                })
                .when(Routes.project, {
                    controller: 'addProject', templateUrl: 'projectTemplate'
                })
				.when(Routes.classify, {
					controller: 'classify', templateUrl: 'classifyTemplate'
				})
                .otherwise({redirectTo: Routes.main});
        }]);