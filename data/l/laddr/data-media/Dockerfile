FROM tutum/ubuntu:trusty  
#FROM debian:latest  
MAINTAINER Warren Legg  
  
#Add Laddr build code  
ADD laddr-run.sh /laddr-run.sh  
RUN chmod 755 /*.sh  
  
# Add temporary media file import area (for test images, or imported images)  
ADD media /tmp/media  
  
#Create directory for media volume  
RUN mkdir -p /usr/laddr/media  
RUN chmod -R 755 /usr/laddr/media  
  
#Override CMD so that laddr-specific run file is called, which calls run.sh in
turn  
CMD ["/laddr-run.sh"]  
  

