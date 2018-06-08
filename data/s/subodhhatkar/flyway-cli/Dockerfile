FROM java:8  
MAINTAINER "Subodh Hatkar" <subodh.hatkar@accenture.com>  
  
ADD http://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/4.2.0/flyway-commandline-4.2.0.zip /  
  
RUN unzip /flyway-commandline-4.2.0.zip && rm /flyway-commandline-4.2.0.zip &&
mv /flyway-4.2.0 /flyway && ln -s /flyway/flyway /usr/local/bin/flyway  
  
# driver for oracle  
COPY drivers/* /flyway/drivers/  
  
# A simple testing  
RUN flyway 2>&1 | grep "Flyway 4.2.0"  
  
WORKDIR /flyway  
ENTRYPOINT ["flyway"]  
CMD ["--help"]  

