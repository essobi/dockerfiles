FROM frolvlad/alpine-python3  
MAINTAINER ponteineptique <thibault.clerice[@]uni-leipzig.de>  
  
# Install required packages  
RUN apk add \--no-cache \  
python3-dev python py-pip nginx supervisor \  
gcc linux-headers libxml2 libxml2-dev libxslt libxslt-dev musl musl-dev  
  
# Sets up locales to avoid decode issue in python  
ENV LANG C.UTF-8  
  
WORKDIR /code/  
  
# Required by supervisor which runs on python 2.7 apparently  
RUN pip2.7 install supervisor-stdout  
  
# Get the main app and configuration files  
# File management (everything after an ADD is uncached) so we do it as late as
possible in the process.  
ADD ./resources ./  
RUN cp ./nginx.conf /etc/nginx/nginx.conf  
ADD ./assets ./static/assets  
ADD ./config ./config  
  
RUN pip3 install -r requirements-py3.txt  
  
VOLUME /opt/data  
VOLUME /opt/cache  
VOLUME /code/static/assets  
VOLUME /code/config  
  
# Expose right ports  
EXPOSE 80  
  
# start supervisor to run our wsgi server  
CMD ["supervisord", "-c", "./supervisord.conf", "-n"]  

