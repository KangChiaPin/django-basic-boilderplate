require! <[ path webpack webpack-bundle-tracker webpack-livereload-plugin ]>
config = require \./webpack.base.config.ls

# Add HotModuleReplacementPlugin and BundleTracker plugins
config.plugins = config.plugins.concat do
  * new webpack.HotModuleReplacementPlugin!
  * new webpack.NoErrorsPlugin! # don't reload if there is an error
  * new webpack-bundle-tracker filename: \./webpack/webpack-stats.json
  * new webpack-livereload-plugin!

config.watch = true

config.devtool = \cheap-module-eval-source-map

module.exports = config
