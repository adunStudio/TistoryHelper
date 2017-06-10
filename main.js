const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

const path = require('path');
const url = require('url');

var mainWindow = null;

app.on('window-all-closed', function() {
    app.quit();
});

app.on('ready', function() {
  var subpy = require('child_process').spawn('python', ['./main.py']);
  var rq = require('request-promise');
  var mainAddr = 'http://localhost:7711';

  var openWindow = function(){
    mainWindow = new BrowserWindow({width: 800, height: 600});
    mainWindow.loadURL('http://localhost:7711/login');
    mainWindow.webContents.openDevTools();
    mainWindow.on('closed', function() {
      mainWindow = null;
      subpy.kill('SIGINT');
    });
  };

  var startUp = function(){
    rq(mainAddr)
      .then(function(htmlString){
        console.log('server started!');
        openWindow();
      })
      .catch(function(err){
        startUp();
      });
  };

  startUp();
});



