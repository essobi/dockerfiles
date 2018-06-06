# docker file to create container with python, flask, uWSGI and nginx  
FROM alpine:latest  
MAINTAINER nasacct  
COPY repositories /etc/apk  
RUN apk update && \  
apk add bash python py-pip uwsgi uwsgi-python nginx ca-certificates supervisor
&& \  
pip install flask flask-session  
# add requirements for gevent  
RUN apk add gcc libc-dev python-dev && \  
pip install gevent  
# configure nginx and uwsgi  
COPY nginx.conf /etc/nginx/  
COPY uwsgi.conf /etc/  
# configure supervisord  
COPY supervisord.conf /etc/  
# create application subdirectories  
RUN mkdir /app  
# copy template  
COPY main.py /app  
WORKDIR /app  
CMD supervisord -c /etc/supervisord.conf  

