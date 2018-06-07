FROM existenz/base  
  
MAINTAINER docker@stefan-van-essen.nl  
  
RUN apk -U add git python unrar && rm -rf /tmp && rm -rf /var/cache/apk/* && \  
git clone \--depth 1 https://github.com/SickRage/SickRage.git /app  
  
EXPOSE 8081  
CMD ["runas", "/usr/bin/python", "/app/SickBeard.py", "--datadir=/home"]  

