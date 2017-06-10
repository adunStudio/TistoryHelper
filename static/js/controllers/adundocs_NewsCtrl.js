
AdunDocs.controller('newsCtrl', ['$scope', '$timeout', function newsCtrl($scope, $timeout) {
    $scope.setDocStat();



    function date_sort(a, b) {
        return new Date(b.btime).getTime() - new Date(a.btime).getTime();
    }

    $scope.sortedFileArray = [];

    $scope.toDateString = function(string) {
        var stringArr = string.split(' ');
        return stringArr[0];// + stringArr[1];
    }

    $scope.$watch('fileTree', function() {
        if( $scope.fileTree ) {
            $scope.sortedFileArray = $scope.fileTree.slice();
            $scope.sortedFileArray.sort(date_sort);
        }
    })


    if( !$scope.isMobile ) {
        var cal = new CalHeatMap();
        var date = new Date;
        date.setMonth(date.getMonth() - 7);
        cal.init({
            itemSelector: "#_heatmap",
            domain: 'month',
            subDomain: 'x_day',
            cellSize: 15,
            subDomainTextFormat: '%d',
            domainGutter: 3,
            domainMargin: [0, 1, 2, 1],
            legendHorizontalPosition: 'right',
            nextSelector: "#map_next",
            previousSelector: "#map_prev",
            colLimit: 5,
            range: 8,
            tooltip: true,
            start: date,
            highlight: "now",
            weekStartOnMonday: true,
            legend: [1, 3, 5, 10],
            data: "./article/news",
            dataType: 'json',
            onClick: function(data, nb) {
                var mm = data.getMonth() + 1; // getMonth() is zero-based
                var dd = data.getDate();

                var yyyymmdd =  [
                    data.getFullYear(),
                    '-',
                    (mm>9 ? '' : '0') + mm,
                    '-',
                    (dd>9 ? '' : '0') + dd
                ].join('');

                var $anchor = $("." + yyyymmdd);
                if( $anchor.length > 0 )
                {
                    $('._content, body').stop().animate({
                        scrollTop: ($anchor.offset().top - 60)
                    }, 1250, 'easeInOutExpo');
                }

            }
        });
    }





}]);
