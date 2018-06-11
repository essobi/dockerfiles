FROM atlassian/bamboo-base-agent  
  
RUN apt-get update -qq && apt-get install -qy \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common  
  
RUN add-apt-repository ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk \  
openjdk-8-jre  
  
RUN echo 2 | update-alternatives --config java && \  
echo 2 | update-alternatives --config javac  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \-
&& \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" && \  
apt-get update -qq && \  
apt-get install -qy docker-ce  
  
RUN curl -sfL
https://github.com/docker/compose/releases/download/1.18.0/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  

