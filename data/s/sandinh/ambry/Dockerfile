FROM sandinh/ambry  
  
COPY config /opt/ambry/config/  
VOLUME /opt/ambry/config  
ENTRYPOINT ["java",
"-Dlog4j.configuration=file:/opt/ambry/config/log4j.properties", "-cp",
"ambry.jar"]  

