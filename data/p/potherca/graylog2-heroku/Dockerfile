FROM heroku/cedar:14  
LABEL namespace="potherca"  
LABEL repository-name="graylog2-heroku"  
LABEL version="0.1.0"  
LABEL short-description="Run Graylog2 on Heroku"  
LABEL full-description="Docker images based on 'heroku/cedar', combining the \  
'phusion/baseimage' and 'graylog2/allinone' images to create an image that can
\  
be run on Heroku using heroku-docker."  
LABEL visibility="public"  
  
MAINTAINER Potherca <potherca@gmail.com>  
  
#WORKDIR './phusion-baseimage-docker/image'  
RUN echo ' =====> Running steps from "phusion/baseimage"'  
#
==============================================================================  
# phusion-baseimage-docker/master/image/Dockerfile  
#
------------------------------------------------------------------------------  
# FROM ubuntu:14.04  
# MAINTAINER Phusion <info@phusion.nl>  
ADD ./phusion-baseimage-docker/image /bd_build  
  
RUN /bd_build/prepare.sh && \  
/bd_build/system_services.sh && \  
/bd_build/utilities.sh && \  
/bd_build/cleanup.sh  
  
CMD ["/sbin/my_init"]  
#
==============================================================================  
RUN echo ' =====> Running steps from "graylog2/allinone"'  
#WORKDIR './graylog2-images/docker'  
#
==============================================================================  
# graylog2-images/master/docker/Dockerfile  
#
------------------------------------------------------------------------------  
# FROM phusion/baseimage:0.9.17  
# MAINTAINER Marius Sturm <hello@torch.sh>  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV JAVA_HOME /opt/graylog/embedded/jre  
  
RUN apt-get update && \  
apt-get install -y curl ntp ntpdate tzdata && \  
curl -O -L https://packages.graylog2.org/releases/graylog-
omnibus/ubuntu/graylog_latest.deb && \  
dpkg -i graylog_latest.deb && \  
rm graylog_latest.deb && \  
sed -i
"0,/^\s*$/s//\/opt\/graylog\/embedded\/share\/docker\/run_graylogctl\n/"
/etc/rc.local && \  
sed -i "0,/^\s*$/s//tail\ \\-F\ \/var\/log\/graylog\/server\/current\ \&\n/"
/etc/rc.local && \  
install -d /opt/graylog/embedded/share/graylog && \  
echo 'GRAYLOG_INSTALLATION_SOURCE="docker"' >
/opt/graylog/embedded/share/graylog/installation-source.sh && \  
apt-get clean && \  
rm -rf /tmp/* /var/tmp/*  
  
VOLUME /var/opt/graylog/data  
VOLUME /var/log/graylog  
VOLUME /opt/graylog/plugin  
VOLUME /opt/graylog/conf/nginx/ca  
  
# web interface  
EXPOSE 9000  
EXPOSE 443  
# gelf tcp  
EXPOSE 12201  
# gelf udp  
EXPOSE 12201/udp  
# rest api  
EXPOSE 12900  
# etcd  
EXPOSE 4001  
# syslog  
EXPOSE 514  
EXPOSE 514/udp  
  
CMD ["/opt/graylog/embedded/share/docker/my_init"]  
#
==============================================================================  
# EOF  

