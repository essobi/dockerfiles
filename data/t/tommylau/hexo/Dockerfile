FROM node:slim  
  
MAINTAINER Tommy Lau <tommy@gen-new.com>  
  
# Install Git, needed to publish to GitHub  
RUN apt-get update && apt-get install -y git ssh-client rsync --no-install-
recommends && rm -r /var/lib/apt/lists/*  
  
# Change timezone to China Standard Time  
RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# Install Hexo  
RUN npm install hexo-cli -g  
  
# Prepare work directory  
RUN mkdir /hexo  
WORKDIR /hexo  
  
EXPOSE 4000  
CMD ["hexo", "server", "-i", "0.0.0.0"]  

