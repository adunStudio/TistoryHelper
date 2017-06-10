
AdunDocs.controller('dirCtrl', ['$scope', '$routeParams','$timeout', function dirCtrl($scope, $routeParams, $timeout) {
    var dirName  =  $routeParams.dirName;
    var check  =  $routeParams.check;


    $scope.setDocStat(dirName);

    $timeout(function() {
        var dirEl =  angular.element(document.getElementById('_' + dirName));

        if( $scope.isToggleCheck == false || check ) {
            $scope.toggleCheck(dirEl);
        }
    }, 0)


}]);