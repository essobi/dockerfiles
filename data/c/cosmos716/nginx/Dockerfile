# cosmos Nginx  
FROM nginx:1.9  
MAINTAINER z2493225@gmail.com  
  
## Add uid 1000  
RUN adduser --disabled-password --gecos "" flashaim  
  
COPY nginx.conf /etc/nginx/  
RUN rm /etc/nginx/conf.d/*  
  
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y --force-yes dist-upgrade  
RUN apt-get install -y --force-yes ffmpeg  
RUN apt-get install -y python-pip  
RUN pip install awscli  
RUN pip install youtube_dl  

