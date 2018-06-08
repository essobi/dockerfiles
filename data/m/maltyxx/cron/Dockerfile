FROM centos:7  
MAINTAINER Yoann VANITOU <yvanitou@gmail.com>  
  
ENV CRON_VERSION 1.4  
ENV DOCKER_VERSION "17.03.1-ce"  
RUN yum -y install cronie-$CRON_VERSION* && yum clean all  
  
# Install Docker client  
RUN curl -L -o /tmp/docker-$VERSION.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz
\  
&& tar -xz -C /tmp -f /tmp/docker-$VERSION.tgz \  
&& mv /tmp/docker/docker /usr/bin \  
&& rm -rf /tmp/docker-$VERSION /tmp/docker  
  
CMD ["/usr/sbin/crond", "-n", "-x", "bit"]  

