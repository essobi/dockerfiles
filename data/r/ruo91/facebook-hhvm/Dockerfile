#  
# Dockerfile - Facebook HHVM  
#  
# - Build  
# docker build --rm -t hhvm:packages /root/docker/production/hhvm  
#  
# - Run  
# docker run -d --name="hhvm" -h "hhvm" -v /tmp:/tmp -v /home:/home
--link=redis:redis--privileged=true hhvm:packages  
# docker run -d --name="hhvm" -h "hhvm" -p 9000:9000 -v /tmp:/tmp -v
/home:/home --link=redis:redis hhvm:packages  
# - SSH  
# ssh `docker inspect -f '{{ .NetworkSettings.IPAddress }}' hhvm`  
FROM ubuntu:15.10  
MAINTAINER Yongbok Kim <ruo91@yongbok.net>  
  
# Repo  
#RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list  
# Last Package Update & Install  
RUN apt-get update && apt-get install -y wget supervisor add-apt-key  
  
# HHVM  
RUN wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add - \  
&& echo 'deb http://dl.hhvm.com/ubuntu wily main' >
/etc/apt/sources.list.d/hhvm.list \  
&& apt-get update && apt-get install -y hhvm libgmp10  
  
# ADD in the hhvm directory  
# http://docs.hhvm.com/manual/en/mysql.configuration.php  
ADD conf/php.ini /etc/hhvm/php.ini  
ADD conf/server.ini /etc/hhvm/server.ini  
  
RUN sed -i "/^PIDFILE=/ s:.*:PIDFILE=/var/run/\$NAME.pid:" /etc/init.d/hhvm  
  
# LANG  
# https://github.com/facebook/hhvm/issues/3112  
RUN echo 'export LANG=C' >> /etc/profile \  
&& echo 'export LC_ALL=C' >> /etc/profile \  
&& echo '' >> /etc/profile  
  
# Supervisor  
RUN mkdir -p /var/log/supervisor  
ADD conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Port  
EXPOSE 9000  
# Daemon  
CMD ["/usr/bin/supervisord"]  

