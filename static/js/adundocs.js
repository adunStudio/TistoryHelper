var AdunDocs = angular.module('AdunDocs', ['ngRoute', 'ngCookies', 'ngSanitize', 'ngMessages']);

AdunDocs.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);


AdunDocs.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when("/view/:postId", {templateUrl: '/static/views/view.html?v=222222221', controller: "ViewCtrl"})
        .when("/write", {templateUrl: '/static/views/write.html?v=22222222222222221', controller: "WriteCtrl"})
        .when('/',        {templateUrl: '/static/views/intro.html?v=2222221'})
        .when('/news',    {templateUrl: '/static/views/news.html?v=122222',    controller: 'NewsCtrl'})
        .otherwise({redirectTo: '/'});
}]);


AdunDocs.controller('DocsCtrl', ['$rootScope', '$scope', '$http', '$routeParams','$location', '$cookies','$interval', function DocsCtrl($rootScope, $scope, $http, $routeParams, $location, $cookies,$interval) {

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

    $scope.togglePost = function(event, el) {
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
    };

    $http.get('/api/info').then(function(response) {
        var data = response.data;
        var tistory = data.tistory.item;
        var blogs = tistory.blogs;
        $scope.blog = blogs[0];
        $scope.blogName = blogs[0].nickname;
        console.dir($scope.blog)
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

    $http.get('/api/guestbook/list').then(function(response) {
        $scope.guestBook = response.data.guestbooks;
     });

     $http.get('/api/comment/newest').then(function(response) {
        $scope.newest = response.data.comments;
     });

     $interval(function() {
            $http.get('/api/guestbook/list').then(function(response) {
             var guestBook = response.data.guestbooks;

             if(guestBook[0].id != $scope.guestBook[0].id)
             {
                 $scope.guestBook = response.data.guestbooks;
                 $scope.notify("새로운 방명록이 달렸습니다.", guestBook[0].name + ":\n" + guestBook[0].comment);
             }
     });

            $http.get('api/comment/newest').then(function(response) {
             var newest = response.data.comments;

             if(newest[0].id != $scope.newest[0].id)
             {
                 $scope.newest = newest;
                 $scope.notify("새로운 댓글이 달렸습니다.", newest[0].name + ":\n" + newest[0].comment);
             }
     });

     }, 1000 * 2);


    $scope.notify = function(title, body) {
        if (Notification.permission !== "granted")
            Notification.requestPermission();
        else {
            var notification = new Notification(title, {
                body: body
            });
            notification.onclick = function(){
                      window.open("http://localhost:7711/#news");

            };
        }
    }




}]);

AdunDocs.controller('ViewCtrl', ['$scope', '$http', '$routeParams', function ViewCtrl($scope, $http, $routeParams) {
    var postId  = $routeParams.postId;
    $scope.main = angular.element(document.querySelector('#main'));


     $http.get('/api/post/read?postId=' + postId).then(function(response) {
        $scope.post = response.data;
        $scope.main.html($scope.post.content);
        $scope.setPost($scope.post);
     });
}]);

AdunDocs.controller('WriteCtrl', ['$scope', '$http', '$routeParams', function WriteCtrl($scope, $http, $routeParams) {
     var converter = converter || new showdown.Converter();

     var editor = $scope.editor = editormd("contents", {
        saveHTMLToTextarea : true,

        imageUploadURL : "./article/upload",
        onfullscreen : function() {
            $scope.$container.css('z-index', '100');
        },
        onfullscreenExit : function() {
            $scope.$container.css('z-index', '1');
        },
    });

     $scope.write = function(event) {
        event.preventDefault();
        var contents = editor.getHTML();
         $http({
                method  : 'POST',
                url     : '/api/post/write',
                data    : {
                    category: $scope.inputCategory,
                    content: contents,
                    title: $scope.inputTitle
                },
                headers : {'Content-Type': 'application/json'}
            }).then(function(response) {
                //$scope.reload();
                location.href = "/";

            });
    };
}]);

AdunDocs.controller('NewsCtrl', ['$scope', '$http', '$routeParams', function NewsCtrl($scope, $http, $routeParams) {
     $http.get('/api/guestbook/list').then(function(response) {
        $scope.guestBook = response.data.guestbooks;
     });

     $http.get('/api/comment/newest').then(function(response) {
        $scope.newest = response.data.comments;
     });
}]);

document.addEventListener('DOMContentLoaded', function () {
  if (Notification.permission !== "granted")
    Notification.requestPermission();
});