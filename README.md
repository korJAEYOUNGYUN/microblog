## Flask-microblog
A micro blog application using flask by [Miguel](https://github.com/miguelgrinberg/microblog).
Details in [here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).



## Dependencies
- elasticsearch
- flask
    - flask-bootstrap
    - flask-httpauth
    - flask-login
    - flask-migrate
    - flask-mail
    - flask-moment
    - flask-sqlalchemy
    - flask-wtf
    
- python-dotenv
- pyjwt
    
## Installation
```shell script
git clone https://github.com/korJAEYOUNGYUN/Flask-microblog.git
pip install -r requirements.txt
```
Also, you have to make `.env` file which contains below secret configs.
```dotenv
SECRET_KEY=%your secret key%
MAIL_SERVER=%your mail server%
MAIL_PORT=%your mail port%
ELASTICSEARCH_URL=%your elasticsearch url%
```