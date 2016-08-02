var path = require("path")
var webpack = require('webpack')
var webpackLivereloadPlugin = require('webpack-livereload-plugin')
var BundleTracker = require('webpack-bundle-tracker')
var config = require('./webpack.base.config.js')

// Add HotModuleReplacementPlugin and BundleTracker plugins
config.plugins = config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoErrorsPlugin(), // don't reload if there is an error
  new BundleTracker({filename: './webpack/webpack-stats.json'}),
  new webpackLivereloadPlugin(),
  new webpack.ProvidePlugin({
    $: "jquery",
    jQuery: "jquery"
  })
])

config.watch = true

module.exports = config
