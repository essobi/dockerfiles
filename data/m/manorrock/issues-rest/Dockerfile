FROM manorrock/openjdk:8  
RUN zypper --non-interactive install wget  
ENV PATH_PREFIX /issues/rest  
ENV ROOT_DIRECTORY /mnt  
ENV SERVER_PORT 8080  
RUN mkdir -p /opt/issues_rest  
WORKDIR /opt/issues_rest  
RUN wget
https://dl.bintray.com/manorrock/maven/com/manorrock/issues/rest/24/rest-24-all.jar  
RUN mv rest-24-all.jar /opt/issues_rest/issues_rest.jar  
WORKDIR /mnt  
CMD ["java", "-XX:+ExitOnOutOfMemoryError", "-jar",
"/opt/issues_rest/issues_rest.jar"]  

