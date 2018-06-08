FROM jsurf/rpi-java  
  
RUN ["cross-build-start"]  
  
RUN apt-get update && apt-get install -y wget  
  
ENV M2_HOME "/opt/apache-maven-3.5.3"  
ENV PATH "$PATH:$M2_HOME/bin"  
COPY ./installmaven.sh /  
RUN chmod +x /installmaven.sh  
  
RUN ["./installmaven.sh"]  
  
CMD ["mvn", "version"]  
  
RUN ["cross-build-end"]  
  

