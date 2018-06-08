FROM prolucid/storm-base:0.0.3  
MAINTAINER Daniel Covello  
  
# Make configure drpc run scripts  
RUN mkdir /etc/service/storm-drpc  
RUN cp /etc/service/storm/run /etc/service/storm-drpc/run  
RUN sed -i -e "s/%STORMAPP%/drpc/g" /etc/service/storm-drpc/run  
RUN chmod +x /etc/service/storm-drpc/run  
# Configure nimbus startup script  
RUN sed -i -e "s/%STORMAPP%/nimbus/g" /etc/service/storm/run  
RUN chmod +x /etc/service/storm/run  
  
EXPOSE 6627  
EXPOSE 3772  
EXPOSE 3773  

