FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y git openjdk-8-jdk maven && \  
rm -rf /var/lib/apt/lists/*  
RUN useradd -ms /bin/bash elastic  
RUN mkdir -p /var/elastic  
RUN cd /var/elastic/ && git clone \--depth=1
https://github.com/OrdinaryDude/elastic-pl.git elastic-pl && cd elastic-pl &&
mvn compile package install  
RUN cd /var/elastic/ && git clone \--depth=1
https://github.com/OrdinaryDude/elastic-core.git && cd elastic-core  
RUN sed -i "s/nxt.allowedUserHosts=127.0.0.1/nxt.allowedBotHosts=*;#/g"
/var/elastic/elastic-core/conf_default/nxt-default.properties  
RUN sed -i "s/nxt.allowedBotHosts=127.0.0.1/nxt.allowedBotHosts=*;#/g"
/var/elastic/elastic-core/conf_default/nxt-default.properties  
RUN sed -i "s/nxt.apiServerHost=127.0.0.1/nxt.apiServerHost=0.0.0.0/g"
/var/elastic/elastic-core/conf_default/nxt-default.properties  
RUN cd /var/elastic/elastic-core && mvn compile package  
RUN cd /var/elastic/elastic-core/ && mkdir conf && cp conf_default/nxt-
default.properties conf/nxt.properties  
RUN chown -R elastic:elastic /var/elastic  
  
VOLUME ["/var/elastic"]  
  
USER elastic  
WORKDIR /var/elastic/elastic-core  
  
CMD ["java","-jar","/var/elastic/elastic-core/target/elastic-core-0.8.0.jar"]  
  
EXPOSE 6876  

