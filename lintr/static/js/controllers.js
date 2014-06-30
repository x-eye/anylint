angular.module('app.controllers', [])
    .controller('main', ['$scope', '$location', 'Status', function($scope, $location, Status) {
		
		Status.get().then(
			function() {
				$location.path('/project')
			}
		)
		
    }])
	.controller('addProject', ['$scope', function($scope) {

    }])
	.controller('classify', ['$scope', function($scope) {
	
	}]);