External Python dependencies:
    django
        pip install django
    pillow
        Required in order to use Django's ImageField.
        pip install pillow
    pandas
        Used to download/process url data and store/retrieve to/from SQL database.
        pip install pandas
    sqlalchemy
        Used with pandas to create SQL database and perform SQL operations on said database.
        pip install SQLAlchemy
    bcrypt
        Password-hashing function used to encrypt user information
        pip install bcrypt
    argon2
        Password-hashing function used to encrypt user information
        pip install django[argon2]
    djangorestframework
        Toolkit for building Web APIs. Installed this for compatibility with ReactJS.
        pip install djangorestframework
    django-cors-headers
        Python library for preventing errors normally triggered due to CORS rules
        pip install django-cors-headers
    python-decouple
        Used to hide the project's SECRET_KEY from public view

External HTML dependencies:
    echarts
        Used to create visual, interactive charts in Javascript
        <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
    jquery
        Javascript library used to simplify HTML DOM tree traversal and manipulation 
        <script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=" crossorigin="anonymous"></script>
    bootstrap
        CSS framework that contains built-in design templates for various HTML components 
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>