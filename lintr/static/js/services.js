angular.module('app.services', [])
    .factory('Ajax', ['$http', '$q', function($http, $q) {
        return {
            get:
                function (action, data) {
					var deferred = $q.defer();
                    var url = "/api/0.0.1/" + action;
                    var params = {
						url: url ,
                        method: "GET"
					};
                    if (data) {
                        params.data = data;
					}
                    $http(params).success(
						function(data, status) {
							deferred.resolve(data, status);
						}
					).error(
						function(status) {
							deferred.reject(status);
						}
					);
					
					return deferred.promise;
                },
				
			post:
                function (action, data) {
					var deferred = $q.defer();
                    var url = "/api/0.0.1/" + action;
                    var params = {
						url: url ,
                        method: "POST"
					};
                    if (data) {
                        params.data = data;
					}
                    $http(params).success(
						function(data, status) {
							deferred.resolve(data, status);
						}
					).error(
						function(status) {
							deferred.reject(status);
						}
					);
					
					return deferred.promise;
                }
        }
    }])
	.service('Status', ['$q', 'Ajax',
        function($q, Ajax) {
		
			var session_status = {
				'stage': 'initial'
			};
		
            this.get = function() {
				var deferred = $q.defer();
				var promise = Ajax.get('session-task-status');
				
				promise.then(
						function(data, status){
							// success
							session_status.stage = data.stage;
							deferred.resolve(data, status);
							// todo: validate data
							// data contains:
							//   stage,
						},
						function(status){
							// error
							deferred.reject(status);
						}
					);
					
				return deferred.promise;
			};
			
			this.resolve = function() {
				
			}			
    }])
	.constant('Routes', {
		project: '/project',
		classify: '/classify',
		main: '/'
    });  