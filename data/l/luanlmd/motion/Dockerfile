FROM ubuntu:zesty  
  
# Basics  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install nano -y  
  
# Motion  
RUN apt-get install motion -y  
  
# Enable daemon mode  
RUN sed -i 's/start_motion_daemon=no/start_motion_daemon=yes/'
/etc/default/motion  
  
# Config  
RUN echo "camera_dir /conf.d" >> /etc/motion/motion.conf  
  
CMD motion  

