FROM ubuntu-upstart:latest  
MAINTAINER Fusengine <info@fusengine.ch>  
  
# Add buildpack  
COPY script_base/ /root  
RUN chmod 775 /root/*.sh  
  
# Run buildpack  
RUN ./root/build_default_pack.sh  
  
# list php7 package  
# RUN apt-cache search php7-*  
# Expose  
EXPOSE 22  
# pepare for takeoff  
CMD ["/sbin/init"]  

