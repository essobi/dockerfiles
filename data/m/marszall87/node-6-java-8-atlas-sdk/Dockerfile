FROM node:6  
  
RUN apt-get update && \  
apt-get install apt-transport-https && \  
# Atlassian SDK  
sh -c 'echo "deb https://sdkrepo.atlassian.com/debian/ stable contrib" >>
/etc/apt/sources.list' && \  
# Oracle Java  
sh -c 'echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
>> /etc/apt/sources.list' && \  
# Accept the Oracle license  
sh -c 'echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections' && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
B07804338C015B73 && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-get update && \  
apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default \  
atlassian-plugin-sdk && \  
rm -rf /var/lib/apt/lists/*  

