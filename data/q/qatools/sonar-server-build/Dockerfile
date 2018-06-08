from dockerfile/java:oracle-java7  
maintainer Baev Dmitry  
  
RUN cd /tmp && \  
curl -L -O http://dist.sonar.codehaus.org/sonarqube-4.5.4.zip && \  
unzip sonarqube-4.5.4.zip && \  
mv sonarqube-4.5.4 /opt/sonar  
  
RUN sed -i 's|#sonar.jdbc.password=sonar|sonar.jdbc.password=123qwe|g'
/opt/sonar/conf/sonar.properties  
RUN sed -i 's|#sonar.jdbc.username=sonar|sonar.jdbc.username=sonar|g'
/opt/sonar/conf/sonar.properties  
RUN sed -i 's|sonar.jdbc.url=jdbc:h2|#sonar.jdbc.url=jdbc:h2|g'
/opt/sonar/conf/sonar.properties  
RUN sed -i
's|#sonar.jdbc.url=jdbc:mysql://localhost|sonar.jdbc.url=jdbc:mysql://${env:DB_PORT_3306_TCP_ADDR}|g'
/opt/sonar/conf/sonar.properties  
  
EXPOSE 9000  
CMD ["/opt/sonar/bin/linux-x86-64/sonar.sh","console"]  

