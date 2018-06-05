FROM openjdk:8-jdk  
MAINTAINER "Richard Simko" <richard@refinedwiki.com>  
  
WORKDIR /opt  
  
RUN apt-get update && sh -c 'echo "deb https://sdkrepo.atlassian.com/debian/
stable contrib" >>/etc/apt/sources.list' && apt-key adv --keyserver
hkp://keyserver.ubuntu.com:80 \--recv-keys B07804338C015B73 && apt-get install
-y apt-transport-https && curl -sL https://deb.nodesource.com/setup_6.x | bash
- && apt-get install -y atlassian-plugin-sdk nodejs  
  
RUN curl https://bootstrap.pypa.io/get-pip.py | python -  
RUN pip install awscli --ignore-installed six  
  
CMD atlas-version && node -v && aws --version  

