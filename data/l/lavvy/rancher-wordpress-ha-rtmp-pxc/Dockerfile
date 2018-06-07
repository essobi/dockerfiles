FROM ubuntu:14.04  
  
MAINTAINER Manel Martinez <manel@nixelsolutions.com>  
  
#add s3fs support from xueshanf/docker-s3fs  
ENV SCRIPT
https://raw.githubusercontent.com/lavvy/buildmachine/master/build.sh  
  
###end here #################################################################  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y python-software-properties software-properties-common
supervisor curl wget  
  
ENV GLUSTER_VOL ranchervol  
ENV GLUSTER_VOL_PATH /var/www  
ENV HTTP_PORT 80  
ENV RTMP_PORT 1935  
ENV HTTP_DOCUMENTROOT ${GLUSTER_VOL_PATH}  
ENV DEBUG 0  
  
RUN mkdir -p /var/log/supervisor ${GLUSTER_VOL_PATH} /usr/src/nginx  
WORKDIR ${GLUSTER_VOL_PATH}  
  
  
RUN mkdir -p /usr/local/bin  
ADD ./bin /usr/local/bin  
RUN chmod +x /usr/local/bin/*.sh  
ADD ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD ./etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg  
ADD ./etc/nginx/sites-enabled/http /etc/nginx/sites-enabled/http  
ADD ./etc/nginx/rtmp /etc/nginx/rtmp  
ADD static /static  
  
EXPOSE 80 1935  
CMD ["/usr/local/bin/run.sh"]  

