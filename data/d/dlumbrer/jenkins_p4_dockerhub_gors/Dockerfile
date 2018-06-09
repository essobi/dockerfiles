FROM jenkins/jenkins:lts  
  
  
  
  
USER root  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y \  
openssh-server \  
libcppunit-dev \  
cmake \  
build-essential \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common  
  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable"  
  
RUN apt-get update && apt-get install -y docker-ce python-pip  
  
RUN pip install pytest  
RUN apt-get install sudo  
  
RUN echo jenkins:jenkins | chpasswd && echo "jenkins ALL=(ALL) ALL" >>
/etc/sudoers  
  
RUN usermod -aG docker jenkins  
  
RUN systemctl enable docker  
  
USER jenkins

