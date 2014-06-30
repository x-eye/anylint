angular.module('app.directives', [])
    .directive('repoLoad', function() {
        return {
            restrict: 'A'
            , controller: ['$scope', 'Ajax',
                function($scope, Ajax) {
					$scope.loadRepo = function(){
						Ajax.post('code')
							.then(
								function(data, status){
									// success
									console.log(data, status);
								},
								function(status){
									// error
									console.log(status);
								}
							);
					};
					$scope.repository = "";
                }]
                , templateUrl: 'repoLoadTemplate'
                , replace: true
                , transclude: true
        }
    });