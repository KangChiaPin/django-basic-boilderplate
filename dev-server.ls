require! <[webpack webpack-dev-server]>
opt = require \./webpack.config

port = 8082
opt.entry.app.unshift "webpack-dev-server/client?http://0.0.0.0:#port/", \webpack/hot/only-dev-server
<-! (new webpack-dev-server webpack(opt), opt.dev-server).listen port, \0.0.0.0
return console.log it if it
console.log 'webpack-dev-server on port 8080'
