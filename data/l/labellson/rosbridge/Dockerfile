FROM ros:kinetic  
MAINTAINER Daniel Laguna <labellson@gmail.com>  
  
# install rosbridge server and supervisord  
RUN apt-get update && apt-get install -y ros-kinetic-rosbridge-suite
supervisor  
RUN mkdir -p /var/log/supervisor  
  
# serup supervisord.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# setup entrypoint  
COPY ./rosbridge_entrypoint.sh /  
  
EXPOSE 9090  
ENTRYPOINT ["/rosbridge_entrypoint.sh"]  
CMD ["/bin/bash"]  

