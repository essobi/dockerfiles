FROM maven:3.3.9-jdk-8  
RUN apt-get update &&\  
apt-get install -y libxml2-utils python3-setuptools &&\  
easy_install3 pip &&\  
pip install awscli --upgrade &&\  
rm -rf /var/lib/apt/lists/*  

