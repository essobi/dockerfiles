FROM java:7  
RUN wget https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/4.0.1/flyway-commandline-4.0.1.tar.gz  
RUN tar -xzf flyway-commandline-4.0.1.tar.gz  
RUN mv /flyway-4.0.1 /flyway  
  
ENV PATH /flyway:$PATH  
WORKDIR /flyway  
  
ENTRYPOINT ["flyway"]  
CMD ["migrate"]  

