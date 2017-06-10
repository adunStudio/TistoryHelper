AdunDocs.controller('DocsCtrl', ['$rootScope', '$scope', '$http', '$routeParams','$location', '$cookies', function DocsCtrl($rootScope, $scope, $http, $routeParams, $location, $cookies) {
    alert(1);
    $http.get('/api/info').then(function(response) {
            cosole.dir(response);
    });

}]);