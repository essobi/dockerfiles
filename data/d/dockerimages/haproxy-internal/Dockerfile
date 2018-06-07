FROM dockerimages/ubuntu-core:14.04  
MAINTAINER Frank Lemanschik @ Direkt SPEED Europe <frank@github.dspeed.eu>
@frank-dspeed  
ENV DOCKER_BUILD 'docker build -t dockerimages/haproxy-internal
git://github.com/dockerimages/haproxy_internal'  
ENV DOCKER_RUN 'echo "$(sudo docker rm -f HAPROXY-INTERNAL) $(sudo docker run
-d -p 80:80 -v /usr/bin/docker:/usr/bin/docker --name=HAPROXY-INTERNAL
--restart=always dockerimages/haproxy-internal)"'  
ENV DOCKER_HOST tcp://172.17.42.1:4243  
RUN apt-get -y update && apt-get -y install haproxy  
ADD ./init-haproxy /sbin/init  
RUN chmod +x /sbin/init  
CMD ["/sbin/init"]  

