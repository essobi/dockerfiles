# CHOSING DEBIAN  
FROM java:7  
MAINTAINER Tim Tegeler <tegeler@creios.net>  
  
# FLYWAY  
ADD https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/4.0.1/flyway-commandline-4.0.1.zip /flyway.zip  
RUN unzip /flyway.zip  
RUN rm /flyway.zip  
RUN mv /flyway-4.0.1 /flyway  
RUN ln -s /flyway/flyway /usr/local/bin/flyway  
  
WORKDIR /migrations  
ENTRYPOINT ["flyway"]  
CMD ["--help"]  

