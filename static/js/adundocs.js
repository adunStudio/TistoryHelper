var AdunDocs = angular.module('AdunDocs', ['ngRoute', 'ngCookies', 'ngSanitize', 'ngMessages']);

AdunDocs.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);


AdunDocs.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        //.when('/',        {templateUrl: 'views/intro.html'})
        /*.when('/about',   {templateUrl: 'views/about.html',    controller: 'AboutCtrl'})
        .when('/aboutkor',{templateUrl: 'views/aboutkor.html', controller: 'AboutCtrl'})
        .when('/news',    {templateUrl: 'views/news.html',    controller: 'newsCtrl'})
        .when('/tips',    {templateUrl: 'views/tips.html', controller: 'AboutCtrl'})*/

        .otherwise({redirectTo: '/'});
}]);


AdunDocs.controller('DocsCtrl', ['$rootScope', '$scope', '$http', '$routeParams','$location', '$cookies', function DocsCtrl($rootScope, $scope, $http, $routeParams, $location, $cookies) {
    $http.get('/api/info').then(function(response) {
            console.dir(response);
        });
}]);