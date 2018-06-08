FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
# Install Flask  
RUN apk --update add \  
python \  
py-pip \  
&& pip install --upgrade pip \  
&& pip install coverage rednose nose \  
&& pip install Flask Flask-Admin Flask-HTTPAuth Flask-Login flask-mongoengine
Flask-RESTful python-telegram-bot gunicorn emoji\  
# Clean up  
&& rm -rf \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/*  
  
# Expose ports  
EXPOSE 80/tcp  
EXPOSE 443/tcp  
  
# Copy init scripts  
COPY rootfs /  
  
  
  
  

