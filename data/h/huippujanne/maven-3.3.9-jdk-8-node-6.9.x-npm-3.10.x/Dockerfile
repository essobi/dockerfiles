FROM maven:3.3.9-jdk-8  
RUN apt-get update &&\  
curl -sL https://deb.nodesource.com/setup_6.x | bash &&\  
apt-get install -y libxml2-utils nodejs python3-setuptools &&\  
easy_install3 pip &&\  
pip install awscli --upgrade &&\  
rm -rf /var/lib/apt/lists/*  

