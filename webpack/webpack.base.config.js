var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: {
    viewer: ['../assets/example/index.ls'], // entry point of our app.
  },

  output: {
    path: path.resolve('./assets/bundles/'),
    filename: "[name].js"
  },

  plugins: [
  ], // add all common plugins here

  module: { // should turn off hot reload in production mode
    loaders: [
      { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader'}, // to transform JSX into JS
      { test: /\.(eot|png|svg|jpg|ttf|woff2?)$/, loader: 'url-loader' },
      { test: /\.css$/, loader: 'style!css' },
      { test: /\.ls$/, loader: 'livescript' },
      { test: /\.pug$/, loader: 'pug-html' },
      { test: /\.styl$/, loader: 'style!css!stylus' },
    ] // add all common loaders here
  },

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
}
