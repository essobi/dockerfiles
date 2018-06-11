FROM openjdk:8  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN wget
http://central.maven.org/maven2/org/jmxtrans/jmxtrans/263/jmxtrans-263.deb  
RUN dpkg -i jmxtrans-263.deb  
  
COPY run-jmxtrans.sh /run-jmxtrans.sh  
RUN chmod 755 /run-jmxtrans.sh  
  
COPY jmxtrans-config.json /jmxtrans-config.json  
  
COPY log4j.xml /log4j.xml  
  
CMD ["/run-jmxtrans.sh"]  

