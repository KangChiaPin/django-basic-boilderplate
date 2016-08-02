require! <[ fs gulp ini webpack webpack-dev-server ]>
spawn = require \child_process .spawn
config = ini.parse fs.read-file-sync \./config.ini \utf-8 .GENERAL

gulp.task \serve:backend !->
  return if config.debug isnt true
  process.env.PYTHONUNBUFFERED = 1
  process.env.PYTHONDONTWRITEBITECODE = 1
  spawn do
    \python3
    [\manage.py, \runserver, \0.0.0.0: + config.dj_port]
    {stdio: \inherit}

gulp.task \default <[ serve:backend ]>

# vi:et:nowrap
