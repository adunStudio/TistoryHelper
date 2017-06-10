
AdunDocs.controller('viewCtrl', ['$scope', '$http', '$routeParams', '$timeout', function viewCtrl($scope, $http, $routeParams, $timeout) {
    var dirName  = $routeParams.dirName;
    var subName  = $routeParams.subName;
    var fileName = $routeParams.fileName;
    var check  =  $routeParams.check;

    //var url = $scope.toURL('/' + dirName + '/' + subName + '/' + fileName);



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

            $('#main').find('a').each(function(i) {
                console.log(i);
                $(this).attr('target', '_blank');
            })
            return;
        }
        else
        {
            var a = editormd.markdownToHTML("main", {
                markdown        : html ,//+ "\r\n" + $("#append-test").text(),
                //htmlDecode      : true,       // 开启 HTML 标签解析，为了安全性，默认不开启
                htmlDecode      : "style,script,iframe",  // you can filter tags decode
                tocm            : true,    // Using [TOCM]
                emoji           : false,
                taskList        : true,
                tex             : true,  // 默认不解析
                flowChart       : false,  // 默认不解析
                sequenceDiagram : false,  // 默认不解析
                view : true
            });

            $('#main').find('a').each(function(i) {
                console.log(i);
                $(this).attr('target', '_blank');
            })
        }






    });

    $timeout(function() {
        $scope.setDocStat(dirName, subName, fileName, $scope.docs[dirName][subName][fileName].btime, $scope.docs[dirName][subName][fileName].mtime);
        var dirEl =  angular.element(document.getElementById('_' + dirName));
        var subEl =  angular.element(document.getElementById('_' + dirName + "_" + subName));
        var fileEl = angular.element(document.getElementById('_' + dirName + "_" + subName + "_" + fileName));

        if( $scope.isToggleCheck == false || check) {
            $scope.toggleCheck(dirEl, subEl, fileEl);
        }
    }, 0)







/*
    $(function() {
        var testEditormdView, testEditormdView2;

        $.get("test.md", function(markdown) {



            //console.log("返回一个 jQuery 实例 =>", testEditormdView);

            // 获取Markdown源码
            //console.log(testEditormdView.getMarkdown());

            //alert(testEditormdView.getMarkdown());
        });

        testEditormdView2 = editormd.markdownToHTML("test-editormd-view2", {
            htmlDecode      : "style,script,iframe",  // you can filter tags decode
            emoji           : true,
            taskList        : true,
            tex             : true,  // 默认不解析
            flowChart       : true,  // 默认不解析
            sequenceDiagram : true,  // 默认不解析
        });
    });*/

}]);