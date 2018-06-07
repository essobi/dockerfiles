FROM abcplusd/dropwizard-base  
  
MAINTAINER priyamm <priyam.gupta@abcplusd.net>  
  
RUN mkdir -p /usr/src/app  
RUN git clone http://priyamm:%40Coding0@github.com/priyamm/testing.git
/usr/src/app  
WORKDIR /usr/src/app  
  
#RUN mvn clean install  
RUN java -jar target/dropwizard-example-1.0.0-rc4-SNAPSHOT.jar db migrate
example.yml  
CMD java -jar target/dropwizard-example-1.0.0-rc4-SNAPSHOT.jar server
example.yml  
  
EXPOSE 9002

