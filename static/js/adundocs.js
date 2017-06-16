var AdunDocs = angular.module('AdunDocs', ['ngRoute', 'ngCookies', 'ngSanitize', 'ngMessages']);

AdunDocs.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);


AdunDocs.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when("/view/:postId", {templateUrl: '/static/views/view.html?v=1', controller: "ViewCtrl"})
        //.when('/',        {templateUrl: 'views/intro.html'})
        /*.when('/about',   {templateUrl: 'views/about.html',    controller: 'AboutCtrl'})
        .when('/aboutkor',{templateUrl: 'views/aboutkor.html', controller: 'AboutCtrl'})
        .when('/news',    {templateUrl: 'views/news.html',    controller: 'newsCtrl'})
        .when('/tips',    {templateUrl: 'views/tips.html', controller: 'AboutCtrl'})*/

        .otherwise({redirectTo: '/'});
}]);


AdunDocs.controller('DocsCtrl', ['$rootScope', '$scope', '$http', '$routeParams','$location', '$cookies', function DocsCtrl($rootScope, $scope, $http, $routeParams, $location, $cookies) {

    $scope.blogName = "소년코딩";
    $scope.categories = {};

    $scope.getLength = function(arr) {
        return arr.length;
    };

    $scope.setPost = function(post) {
        $scope.post = post;
    };

    $scope.toggle = function(event, el) {
        var element = el || angular.element(event.target);

        if($scope.focus && $scope.active)
        {
             $scope.focus.removeClass('focus');
            $scope.active.removeClass('active');
        }

        element.addClass('active');
        element.addClass('focus');
        $scope.active = element;
        $scope.focus = element;

        if(element.hasClass('open')) {
            element.removeClass('open');
            element.removeClass('open-title');
        }
        else {
            element.addClass('open');
            element.addClass('open-title');
        }
    };

    $http.get('/api/info').then(function(response) {
        var data = response.data;
        var tistory = data.tistory.item;
        var blogs = tistory.blogs;
        $scope.blogName = blogs[0].nickname;
    });

    $http.get('/api/category').then(function(response) {
        var c = response.data.categories;

        for(var i = 0, length = c.length; i < length; ++i)
        {
            var category = c[i];
            $scope.categories[category.id] = category;
            $scope.categories[category.id]["posts"] = [];

            (function(id) {
                 $http.get('/api/post/list?categoryId=' + id).then(function(response) {
                     if(response.data.posts)
                     {
                        $scope.categories[id]["posts"] = response.data.posts;
                     }
                 });
            })(category.id);
        }
    });


}]);

AdunDocs.controller('ViewCtrl', ['$scope', '$http', '$routeParams', function viewCtrl($scope, $http, $routeParams) {
    var postId  = $routeParams.postId;
    $scope.main = angular.element(document.querySelector('#main'));


     $http.get('/api/post/read?postId=' + postId).then(function(response) {
        $scope.post = response.data;
        $scope.main.html($scope.post.content);
        $scope.setPost($scope.post);
     });
}]);