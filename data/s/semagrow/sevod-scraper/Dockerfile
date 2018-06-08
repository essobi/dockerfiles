FROM java:7-jdk  
  
MAINTAINER Yiannis Mouchakis <gmouchakis@iit.demokritos.gr>  
  
RUN apt-get update && apt-get install -y maven && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
RUN git clone https://github.com/semagrow/sevod-scraper.git && \  
cd sevod-scraper && \  
mvn clean install  
  
WORKDIR /sevod-scraper  
  
COPY log4j.properties /sevod-scraper/target/classes/  
  
ENTRYPOINT ["/sevod-scraper/sevod-scraper.sh"]  

