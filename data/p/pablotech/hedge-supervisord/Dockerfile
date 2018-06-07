#FROM pablotech/hedge-ubuntu:latest  
FROM pablotech/hedge-vnc:latest  
  
# SUPERVISORD  
RUN echo "/usr/bin/supervisord" >>/etc/rc.local  
RUN echo "[supervisord]" >>/etc/supervisor/supervisord.conf  
RUN echo "nodaemon=true" >>/etc/supervisor/supervisord.conf  
  

