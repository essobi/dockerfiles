FROM ubuntu:trusty  
  
MAINTAINER Yuvi Panda <yuvipanda@riseup.net>  
  
RUN sudo apt-get update  
RUN sudo apt-get install --yes lighttpd php5-cgi  
RUN mkdir -p /data/project/test  
RUN chown -R www-data:www-data /data  
  
ADD . /data/project/test/  
  
EXPOSE 8080 8090  
ENTRYPOINT /usr/sbin/lighttpd -f /data/project/test/test.conf -D  

