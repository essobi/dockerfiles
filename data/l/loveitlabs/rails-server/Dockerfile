FROM loveitlabs/base2:latest  
MAINTAINER LoveItLabs Team <team@loveItLabs.io>  
  
  
ENV TERM vt100  
ENV GITBRANCH master  
ENV APPROOT app  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y software-properties-common  
RUN sudo add-apt-repository ppa:mc3man/trusty-media  
RUN apt-get update --fix-missing  
RUN apt-get upgrade -y  
  
# Install ruby dependencies  
RUN apt-get install -y \  
mysql-client \  
vim \  
nginx \  
htop \  
imagemagick \  
libmagickwand-dev \  
nodejs \  
supervisor  
  
  
RUN sudo apt-get install -y ffmpeg gstreamer0.10-ffmpeg  
  
  
  
#### Nginx ####  
RUN rm /etc/nginx/sites-enabled/default  
#ADD etc/nginx/$APPROOT /etc/nginx/sites-enabled/  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
  
  
  
RUN mkdir -p /$APPROOT/tmp/pids && chmod 777 /$APPROOT/tmp/pids &&\  
mkdir -p /$APPROOT/log && chmod 777 /$APPROOT/log &&\  
mkdir -p /$APPROOT/tmp/sockets/  
  
  
ADD looper.sh /bin/  
RUN chmod 777 /bin/looper.sh  

