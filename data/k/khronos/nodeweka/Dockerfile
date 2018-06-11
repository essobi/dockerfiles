FROM node:6-wheezy  
  
WORKDIR /srv  
RUN apt-get update  
RUN apt-get install -y unzip openjdk-7-jre  
RUN wget -qO- -O tmp.zip
https://prdownloads.sourceforge.net/weka/weka-3-8-0.zip  
RUN unzip -q tmp.zip  
RUN rm tmp.zip  
WORKDIR /srv/weka-3-8-0  
RUN rm -r wekaexamples.zip weka-src.jar WekaManual.pdf  
RUN rm -r COPYING README changelogs doc documentation.css documentation.html
weka.gif  
ENV CLASSPATH /srv/weka-3-8-0/weka.jar  
  
# Install dependencies  
RUN npm install -g forever  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
RUN npm install -g less  

