# Agave ToGo Dockerfile  
#  
# Docker Repository tag: mfeng/tropdisease  
#  
# https://bitbucket.org/maryfeng/tropdisease  
#  
# Pull base image.  
FROM dockerfile/nodejs  
  
RUN npm install -g yo grunt-cli bower  
  
RUN apt-get install -y ruby  
  
RUN gem install saas compass  
  
RUN \  
cd /tmp && \  
git clone https://bitbucket.org/maryfeng/tropdisease.git  
  
RUN \  
cd /tmp/tropdisease && \  
npm install  
  
RUN \  
cd /tmp/tropdisease && \  
bower install --allow-root -f  
  
# RUN \  
# cd /tmp/tropdisease && \  
# grunt build  
# EXPOSE 9000  
ADD Gruntfile.js /tmp/tropdisease/Gruntfile.js  
  
EXPOSE 9000  
WORKDIR /tmp/tropdisease  
  
# Define default command.  
ENTRYPOINT grunt server  

