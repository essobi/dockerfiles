# Bower builder image  
FROM library/node as bowerbuilder  
  
WORKDIR /app/  
RUN npm install -g bower && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
ADD /.bowerrc /app/.bowerrc  
ADD bower.json /app/bower.json  
RUN bower install  
  
##  
## RUNTIME IMAGE  
##  
FROM python:3-alpine  
  
# install nginx, bower & config  
RUN apk add --no-cache nginx zlib-dev libjpeg-turbo-dev \  
&& mkdir -p /run/nginx/  
ADD docker/django.conf /etc/nginx/django.conf  
  
# our python is in app  
ENV PYTHONPATH /app  
  
# Install Django App and setup the setting module  
ADD api /app/api  
ADD dreamjub /app/dreamjub  
ADD jacobsdata /app/jacobsdata  
ADD login /app/login  
ADD portal /app/portal  
ADD static /app/static/  
ADD widgets /app/widgets  
# ADD .bowerrc /app/.bowerrc  
# ADD bower.json /app/bower.json  
ADD check_pep8.py /app/check_pep8.py  
ADD manage.py /app/manage.py  
ADD requirements.txt /app/requirements.txt  
  
ENV DJANGO_SETTINGS_MODULE "dreamjub.docker_settings"  
# /entrypoint.sh  
ADD docker/entrypoint.sh /entrypoint.sh  
  
# Add the entrypoint and add configuration  
WORKDIR /app/  
  
# Install python deps  
RUN mkdir -p /var/www/static \  
&& apk add --no-cache --virtual pybuilddeps build-base \  
&& pip install -r requirements.txt \  
&& pip install gunicorn==19.7 \  
&& apk del pybuilddeps  
  
# Install bower deps from above  
COPY \--from=bowerbuilder /app/static/components/ /app/static/components/  
  
### ALL THE CONFIGURATION  
# The secret key used for django  
ENV DJANGO_SECRET_KEY ""  
# A comma-seperated list of allowed hosts  
ENV DJANGO_ALLOWED_HOSTS "localhost"  
# Database settings  
## Use SQLITE out of the box  
ENV DJANGO_DB_ENGINE "django.db.backends.sqlite3"  
ENV DJANGO_DB_NAME "/data/dreamjub.db"  
ENV DJANGO_DB_USER ""  
ENV DJANGO_DB_PASSWORD ""  
ENV DJANG_DB_HOST ""  
ENV DJANGO_DB_PORT ""  
# Email settings  
## Use SMTP out of the box  
ENV EMAIL_BACKEND "django.core.mail.backends.smtp.EmailBackend"  
ENV EMAIL_HOST ""  
ENV EMAIL_PORT "587"  
ENV EMAIL_HOST_USER "noreply@jacobs.university"  
ENV EMAIL_HOST_PASSWORD ""  
ENV EMAIL_USE_TLS "1"  
# Sesame settings, should work out of the box  
ENV SESAME_TOKEN_NAME "thanks_irc_it"  
ENV SESAME_MAX_AGE 1800  
# Sesame settings  
# Volume and ports  
VOLUME /data/  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]

