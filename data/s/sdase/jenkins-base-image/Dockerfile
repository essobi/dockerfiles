FROM jenkins/jenkins:2.89.4  
USER root  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common  
RUN cd /tmp && curl -fsSL https://download.docker.com/linux/debian/gpg >
./docker-key && apt-key add ./docker-key && rm docker-key && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/debian \  
$(lsb_release -cs) \  
stable"  
RUN apt-get update && apt-get install -y docker-ce  
RUN usermod -aG docker jenkins  
RUN cd /usr/local/bin && curl -LO https://storage.googleapis.com/kubernetes-
release/release/$(curl -s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x kubectl &&
chown jenkins kubectl && chmod u+x kubectl  
USER jenkins  

