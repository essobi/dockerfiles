FROM reinblau/lamp  
  
MAINTAINER hinx  
  
RUN apt-get update -y  
RUN apt-get install git -y  
RUN apt-get install openjdk-7-jre -y  
  
RUN rm -fr /var/www/html  
RUN git clone https://github.com/hinxcode/codefine.git /var/www/html  
# COPY . /var/www/html  
EXPOSE 80 443

