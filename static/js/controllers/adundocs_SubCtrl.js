
AdunDocs.controller('subCtrl', ['$scope', '$routeParams','$timeout', function subCtrl($scope, $routeParams, $timeout) {
    var dirName  =  $routeParams.dirName;
    var subName  =  $routeParams.subName;
    var check  =  $routeParams.check;


    $scope.setDocStat(dirName, subName);



    $timeout(function() {
        var dirEl =  angular.element(document.getElementById('_' + dirName));
        var subEl =  angular.element(document.getElementById('_' + dirName + "_" + subName));
        if( $scope.isToggleCheck == false || check ) {
            $scope.toggleCheck(dirEl, subEl);
        }
    }, 0)


}]);