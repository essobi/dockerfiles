FROM java:8-jre  
MAINTAINER Eduardo Ivan Pichler  
  
RUN mkdir /usr/local/ceploops  
RUN curl -L -o /usr/local/ceploops/ceploops.jar
https://www.dropbox.com/s/9zxssx0bto1x2yx/ceploops-1.0.14.jar?dl=1  
  
WORKDIR /usr/local/ceploops  
  
EXPOSE 8080  
ENV CEPLOOPS_VERSION=1.0.14  
ENV LUPAZUL_JDBC_URL url  
ENV LUPAZUL_JDBC_PASSWORD pass  
ENV LUPAZUL_JDBC_USER user  
LABEL "Ceploops version"=${CEPLOOPS_VERSION}  
LABEL description="The Ceploops REST service."  
  
CMD ["java", "-jar", "-Dlogback.configurationFile=./logback.xml",
"-Dlogging.config=./logback.xml", "ceploops.jar"]  

