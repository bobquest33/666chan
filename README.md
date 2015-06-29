#Imageboard in Flask and Angular.js


##Running The Backend

Currently, you need two environment variables set:

* `DATABASE_URL`: The database URL, in the format `adapter://user:password@host/db`
* `APP_SETTINGS`: The App Settings class, defined in `backend/config.py`, in the format `config.DevelopmentConfig`.

A good way to have those variables set in development is to add `export` directives to your `$VIRTUAL_ENV/bin/postactivate`.

##Dependencies

All dependencies are listed in the `backend/requirements.txt` file, which can be used to run `pip install -r backend/requirements.txt`.
