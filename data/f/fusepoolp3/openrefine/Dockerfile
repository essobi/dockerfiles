FROM ubuntu:trusty  
  
ADD install-refine.sh install-refine.sh  
RUN chmod +x install-refine.sh  
RUN ./install-refine.sh  
ENV JAVA_OPTIONS='-XX:PermSize=512m -XX:MaxPermSize=512m'  
EXPOSE 3333  
CMD ["/start.sh"]  

