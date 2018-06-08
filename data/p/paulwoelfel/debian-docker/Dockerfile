FROM debian:stretch  
MAINTAINER github@frig.at  
  
ARG DOCKER_VERSION=""  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install \  
apt-transport-https \  
ca-certificates \  
curl \  
gettext \  
gnupg2 \  
software-properties-common \  
&& \  
# rm -rf /var/lib/apt/lists/*  
(curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -) && \  
(add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable") && \  
apt-get update && \  
apt-get -y install \  
docker-ce=$(apt-cache show docker-ce | grep 'Version:' | awk '{print $NF}' |
grep "$DOCKER_VERSION" | head -n 1) && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

