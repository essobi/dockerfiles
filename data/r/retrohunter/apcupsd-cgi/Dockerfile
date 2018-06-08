# APC UPS Power Management  
FROM phusion/baseimage  
  
# update  
RUN apt-get -y update  
  
# install  
RUN apt-get -y install apcupsd  
  
ADD startup.sh /  
  
# clean  
RUN apt-get clean  
  
# Port  
EXPOSE 3551  
CMD /startup.sh;  

