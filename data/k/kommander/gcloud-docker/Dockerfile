FROM google/cloud-sdk:171.0.0  
LABEL name=gcloud-docker  
LABEL version="1.2"  
  
# Install missing Docker dependencies  
RUN apt-get update && apt-get install -y gnupg2 software-properties-common
gettext && apt-get clean  
  
# Add Docker to apt repositories  
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add -  
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(.
/etc/os-release; echo "$ID") $(lsb_release -cs) stable"  
  
# Install Docker CE  
RUN apt-get update && apt-get install -y docker-ce && apt-get clean  

