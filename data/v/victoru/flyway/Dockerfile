FROM java:7  
ADD https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/4.2.0/flyway-commandline-4.2.0.zip /flyway.zip  
  
RUN unzip /flyway.zip && rm /flyway.zip && mv /flyway-4.2.0 /flyway && ln -s
/flyway/flyway /usr/local/bin/flyway  
  
# A simple testing  
RUN flyway 2>&1 | grep "Flyway 4.2.0"  
  
WORKDIR /flyway  
ENTRYPOINT ["flyway"]  
CMD ["--help"]  

