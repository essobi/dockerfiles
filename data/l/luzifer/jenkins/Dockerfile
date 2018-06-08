FROM jenkins/jenkins:2.107.1  
USER root  
  
RUN bash -c "if ! [ -e /usr/lib/apt/methods/https ]; then apt-get update &&
apt-get install -y apt-transport-https; fi"  
  
RUN set -ex \  
&& apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
9DC858229FC7DD38854AE2D88D81803C0EBFCD88 \  
&& sh -c "echo deb [arch=amd64] https://download.docker.com/linux/debian
jessie stable > /etc/apt/sources.list.d/docker.list" \  
&& apt-get update && apt-get install -y docker-ce \  
&& apt-get install -y sudo \  
&& echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
USER jenkins  

