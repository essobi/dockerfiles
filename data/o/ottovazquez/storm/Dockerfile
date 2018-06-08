FROM ottovazquez/storm-base:1.0.2  
MAINTAINER Otto Vazquez  
  
# Nimbus  
EXPOSE 3772 3773 6627  
# Supervisor  
EXPOSE 6700 6701 6702 6703  
# UI  
EXPOSE 8080  
# Logviewer  
EXPOSE 8000  
RUN echo -e '\n\  
storm dev-zookeeper &\n\  
storm nimbus &\n\  
storm supervisor &\n\  
storm ui &\n\  
storm logviewer &\n\  
tail -f /dev/null' >> /entrypoint  

