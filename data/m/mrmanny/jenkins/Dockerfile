FROM jenkins/jenkins  
USER root  
RUN apt-get update &&\  
apt-get install -y python3-pip python3-setuptools python3-all debhelper curl
wget libcurl4-openssl-dev vim libssl-dev make pylint  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
USER jenkins  
HEALTHCHECK CMD curl --fail http://localhost:8080/jenkins || exit 1  

