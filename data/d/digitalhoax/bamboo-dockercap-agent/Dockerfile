FROM atlassian/bamboo-java-agent  
  
RUN apt-get update && apt-get install -y \  
python-software-properties \  
software-properties-common \  
openssh-client  
  
RUN add-apt-repository ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk \  
openjdk-8-jre  
  
RUN apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add \-
&& \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get install -y docker-ce  
  
RUN echo 2 | update-alternatives --config java && \  
echo 2 | update-alternatives --config javac  

