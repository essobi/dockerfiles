FROM jenkins/jenkins:lts  
USER root  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt &&
\  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -yy && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yy \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common &&\  
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | \  
apt-key add - && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) stable" && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yy docker-ce && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

