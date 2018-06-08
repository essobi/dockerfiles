# use node:8 as base image  
FROM node:8  
ENV DOCKER_VERSION 17.12.0~ce-0~debian  
  
# install docker  
RUN apt-get update \  
&& apt-get -y install \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common \  
&& curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add - \  
&& apt-key fingerprint 0EBFCD88 \  
&& add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable" \  
&& apt-get update \  
&& apt-get -y install docker-ce=${DOCKER_VERSION} \  
&& rm -rf /var/cache/apt  
  
# below files are taken from docker's own image  
# see here: https://github.com/docker-library/docker/tree/master/17.12  
# see license DOCKER-LICENSE  
COPY modprobe.sh /usr/local/bin/modprobe  
COPY docker-entrypoint.sh /usr/local/bin/  
  
# the entry point script is needed mainly  
# to support use of docker:dind  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD [ "node" ]

