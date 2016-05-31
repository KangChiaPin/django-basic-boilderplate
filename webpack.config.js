var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var config = require('./webpack.base.config.js')
var port = 8082

// Add HotModuleReplacementPlugin and BundleTracker plugins
config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin(), // don't reload if there is an error
  new BundleTracker({filename: './webpack-stats.json'}),
])
config.devServer = {
  contentBase: './assets/bundles/',
  publicPath: '/assets/bundles',
  host: '0.0.0.0',
  hot: true,
  inline: true,
  stats: {
    chunkModules: false, // do not show list of hundreds of files included in a bundle
    colors: true,
  }
}
module.exports = config
