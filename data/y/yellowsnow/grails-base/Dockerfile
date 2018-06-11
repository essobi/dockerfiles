FROM makuk66/docker-oracle-java7  
  
WORKDIR /opt/grails  
  
ADD grails /opt/grails  
  
RUN ./grailsw refresh-dependencies  
  
ENTRYPOINT ["/bin/bash", "/opt/grails/grailsw"]  
CMD ["-version"]  

