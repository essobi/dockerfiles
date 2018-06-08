# pull base image  
FROM skyscrapers/ansible:ubuntu15.10-onbuild  
MAINTAINER Skyscrapers <support@skyscrapers.eu>  
  
RUN apt-get update && \  
apt-get install -y git gnome-schedule python-pip \  
ruby-full build-essential rake && \  
gem install serverspec  
  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
echo "===> Updating TLS certificates..." && \  
apt-get install -y openssl ca-certificates  
  
ONBUILD WORKDIR /tmp  
ONBUILD COPY . /tmp  
ONBUILD RUN \  
echo "===> Diagnosis: host information..." && \  
ansible -c local -m setup all  

