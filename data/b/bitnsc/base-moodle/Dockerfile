FROM liling/phusion-nginx-php5:5.5  
MAINTAINER liling@bit.edu.cn  
  
RUN apt-get update ; apt-get install -y paps ttf-wqy-microhei ttf-dejavu-core
ttf-freefont libpango1.0-0 cups-client clamav ; apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Startup clamav  
RUN mkdir /etc/service/clamav  
ADD services/clamav.sh /etc/service/clamav/run  
RUN chmod +x /etc/service/clamav/run  

