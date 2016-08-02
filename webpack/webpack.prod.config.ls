require! <[ path webpack webpack-bundle-tracker ]>
config = require \./webpack.base.config.ls
config.output.path = path.resolve \static/bundles

config.plugins = config.plugins.concat do
  * new webpack-bundle-tracker filename: \./webpack/webpack-stats-prod.json

  # removes a lot of debugging code in React
  * new webpack.DefinePlugin {
    'process.env':
      'NODE_ENV': JSON.stringify \production
    }

    # keeps hashes consistent between compilations
  * new webpack.optimize.OccurenceOrderPlugin!

    # minifies your code
  * new webpack.optimize.UglifyJsPlugin {
    compressor: {-warnings}
    }

module.exports = config

