############################################################  
# Dockerfile to build Ubuntu based NTPsec daemon images  
############################################################  
  
FROM ubuntu  
MAINTAINER srinsriv@gmail.com  
  
########  
# PORTS  
########  
# Expose the default port  
EXPOSE 22  
EXPOSE 8080  
EXPOSE 80  
EXPOSE 123/udp  
# Set default container command  
ENV DEBIAN_FRONTEND noninteractive  
  
##############  
# DEPENDENCIES  
##############  
# Update container with libraries needed to compile NTPsec  
RUN apt-get -y update  
RUN apt-get -y install ntp  
  
WORKDIR "/ntp/"  
  
##################  
# SETUP SUPERVISOR  
##################  
  
# Set default container command  
CMD ["/sbin/init"]  

