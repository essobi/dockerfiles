FROM netflixoss/exhibitor:1.5.2  
ADD exhibitor.properties /exhibitor/exhibitor.properties  
ADD wrapper.sh /exhibitor/wrapper.sh  
  
EXPOSE 8080 2181 2888 3888  
WORKDIR /exhibitor  
  
ENTRYPOINT ["/exhibitor/wrapper.sh"]  

