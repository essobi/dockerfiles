FROM linuxbrew/linuxbrew:1.6.3  
RUN sudo apt-get update  
RUN brew -v  
  
# faas cli install  
RUN brew install faas-cli  
RUN faas-cli version  
  
# docker install  
RUN set -x &&\  
VER="17.03.0-ce" &&\  
curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz &&\  
tar -xz -C /tmp -f /tmp/docker-$VER.tgz &&\  
sudo mv /tmp/docker/* /usr/bin  
RUN docker -v  
  
# rancher install  
RUN curl -L -o ./rancher.tar.gz
https://github.com/rancher/cli/releases/download/v2.0.1-rc1/rancher-linux-
amd64-v2.0.1-rc1.tar.gz &&\  
tar xvzf ./rancher.tar.gz &&\  
sudo mv ./rancher-v2.0.1-rc1/rancher /usr/bin &&\  
rm ./rancher.tar.gz &&\  
rm -rf rancher-v2.0.1-rc1  
RUN rancher -v  

