FROM jenkins/jnlp-slave:latest  
LABEL maintainer="Todd Edwards <todd@mtn.cc>"  
LABEL homepage="https://github.com/triangletodd/docker-jnlp-agent-gcloud"  
  
USER root  
RUN apt update && \  
apt install -y apt-utils lsb-release pcregrep && \  
echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c -s)
main" | \  
tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update && \  
apt-get install -y google-cloud-sdk kubectl && \  
groupadd -g 999 ubdocker && \  
usermod -a -G ubdocker jenkins && \  
ln -s /usr /google-cloud-sdk && \  
apt-get install -y apt-transport-https ca-certificates curl software-
properties-common && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get install -y docker-ce python python-pip && \  
pip install --upgrade awsebcli  
# ln's are hack for old builds, FIXME  

