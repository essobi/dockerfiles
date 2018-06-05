ARG VERSION=2.107.3  
FROM jenkins/jenkins:${VERSION:-LTS}  
  
# Prevent the banner from appearing prompting the user to install additional
plugins  
RUN echo ${VERSION:-2.0} >
/usr/share/jenkins/ref/jenkins.install.InstallUtil.lastExecVersion  
  
# Install docker so we can launch dind containers  
USER root  
RUN apt-get update \  
&& apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common \  
&& curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \  
&& add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable" \  
&& apt-get update \  
&& apt-get install -y docker-ce \  
&& usermod -aG docker jenkins  
USER jenkins  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  

