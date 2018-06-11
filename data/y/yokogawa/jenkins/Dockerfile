FROM jenkins:latest  
MAINTAINER yokogawa-k "yokogawa-k@klab.com"  
USER root  
RUN groupadd -g 999 docker  
RUN groupmod -g 9001 jenkins && usermod -a -u 9001 -G 999 jenkins  
#RUN chown jenkins. /var/log/copy_reference_file.log  
RUN cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN curl -L https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz | tar
xzf - --strip-components=1 docker/docker \  
&& mv docker /usr/bin/docker \  
&& chmod +x /usr/bin/docker  
USER jenkins  

