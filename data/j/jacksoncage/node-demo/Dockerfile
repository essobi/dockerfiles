# Node.js demo in container  
#  
# docker run -rm -i -d \  
# -p 8080 \  
# -v /etc/localtime:/etc/localtime \  
# jacksoncage/node-demo  
FROM jacksoncage/node  
MAINTAINER Love Nyberg "love.nyberg@lovemusic.se"  
ENV REFRESHED_AT 2015-12-11  
# Add node application into container  
COPY src /var/www  
  
# Install node dependences  
RUN cd /var/www && npm install  

