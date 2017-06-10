var converter = converter || new showdown.Converter();

AdunDocs.controller('searchCtrl', ['$scope', '$http', '$routeParams', '$timeout', function searchCtrl($scope, $http, $routeParams, $timeout) {
    var dirName  = $routeParams.dirName;
    var subName  = $routeParams.subName;
    var fileName = $routeParams.fileName;


    var url = $scope.toURL('/' + dirName + '/' + subName + '/' + fileName);


    $http({
        method  : 'POST',
        url     : './article/view',
        data    : {
            dirName: dirName,
            subName: subName,
            fileName: fileName
        },
        headers : {'Content-Type': 'application/json'}
    }).then(function (response) {
        var html = response.data.fileData;

        var type = response.data.type;

        if( type == 'html' )
        {
            $('#main').html(html);
            $('#main').find('pre code').each(function(i, block) {
                hljs.highlightBlock(block);
            });
            return;
        }

        var a = editormd.markdownToHTML("main", {
            markdown        : html ,//+ "\r\n" + $("#append-test").text(),
            //htmlDecode      : true,       // ?? HTML ??解析，?了安全性，默?不??
            htmlDecode      : "style,script,iframe",  // you can filter tags decode
            tocm            : true,    // Using [TOCM]
            emoji           : false,
            taskList        : true,
            tex             : true,  // 默?不解析
            flowChart       : false,  // 默?不解析
            sequenceDiagram : false,  // 默?不解析
            view : true
        });
    });


    $scope.setDocStat(dirName, subName, fileName, $scope.docs[dirName][subName][fileName].btime, $scope.docs[dirName][subName][fileName].mtime);

}]);