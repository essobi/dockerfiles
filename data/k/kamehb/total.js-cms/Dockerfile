FROM node:latest  
MAINTAINER KaMeHb-UA "marlock@etlgr.com"  
# Getting sources list  
RUN apt-get update  
# Installing graphicsmagick  
RUN apt-get install -y --no-install-recommends graphicsmagick  
# Installing temporary apps  
RUN apt-get install -y --no-install-recommends unzip  
# Installing Total.js CMS  
RUN mkdir /cms && cd /cms && wget https://github.com/KaMeHb-UA/total.js-cms-
releases/raw/master/sourcecode.zip -O temp.zip && unzip temp.zip && rm
temp.zip && npm install  
# Removing temporary apps  
RUN apt-get remove -y unzip  
# Removing sources list  
RUN rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8000  
CMD ["bash", "-c", "cd /cms && node debug.js"]  
  

