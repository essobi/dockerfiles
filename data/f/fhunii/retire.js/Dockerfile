FROM node  
  
MAINTAINER Timo Pagel <retirejsmaintainer@timo-pagel.de>  
  
RUN npm install -g retire  
  
ADD retire.bash /opt/retire.bash  
  
RUN chmod 555 /opt/retire.bash  
  
ENTRYPOINT ["/opt/retire.bash"]  

