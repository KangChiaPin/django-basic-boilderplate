require! <[ path webpack ]>
module.exports =
  context: __dirname

  entry:
    example: \../assets/example/index.ls # entry point of our app.

  output:
    path: path.resolve \./static/bundles/
    public-path: \/static/bundles/
    filename: '[name].js'

  plugins: [
  ], # add all common plugins here

  module:
    loaders:
      * test: /\.(eot|png|svg|jpg|ttf|woff2?)$/ loader: \url-loader?limit=8192?limit=8192
      * test: /\.css$/ loader: \style!css
      * test: /\.ls$/ loader: \livescript
      * test: /\.styl$/ loader: \style!css!stylus

  resolve:
    modules-directories: [\node_modules]
    extensions: ['', \.js]

  stylus:
    import: [\~nib/lib/nib/index.styl]
    use: [require \nib]
