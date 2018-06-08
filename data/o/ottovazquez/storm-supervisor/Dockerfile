FROM ottovazquez/storm-base:1.0.2  
MAINTAINER Otto Vazquez  
  
EXPOSE 6700 6701 6702 6703  
EXPOSE 8000  
RUN echo -e '\n\  
storm supervisor &\n\  
storm logviewr &\n\  
tail -f /dev/null' >> /entrypoint  

