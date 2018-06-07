FROM fourgeo/android-dev:latest  
  
MAINTAINER Ivan Fastov "c0d3r85@gmail.com"  
RUN apt-get update  
  
# Installing NodeJS  
ADD
["https://raw.githubusercontent.com/nodesource/distributions/master/deb/setup_0.12",
"/tmp/nodesetup.sh"]  
RUN bash /tmp/nodesetup.sh && apt-get install -y
nodejs=0.12.14-1nodesource1~xenial1 && node -v  
RUN npm install -g npm  
  
# Installing Ionic  
RUN npm install -g ionic cordova gulp  

