FROM debian:8  
MAINTAINER Paul Smith <code@uvwxy.de>  
  
# Reload local package  
RUN apt-get update  
  
# Install required tools  
RUN apt-get install -y \  
git \  
libfontconfig1 \  
libfreetype6 \  
nodejs \  
npm \  
python-software-properties  
# Cleanup downloaded *.deb files  
RUN apt-get clean  
  
# Fetch HabitRPG  
RUN git clone https://github.com/HabitRPG/habitrpg.git  
  
# Fix nodejs vs node command  
RUN cd /usr/bin/ && ln -s nodejs node  
  
# Install HabitRPG build dependencies  
RUN npm install -g grunt-cli bower phantomjs  
  
# Setup HabitRPG environment  
RUN cd /habitrpg && npm install && bower install --allow-root  
  
ADD config.json /habitrpg/  
  
EXPOSE 3000  
WORKDIR /habitrpg/  
CMD ["npm", "start"]

