FROM bleshik/scala:2.11.5  
MAINTAINER TSoftware  
ADD / /api  
WORKDIR /api  
RUN sbt test && sbt stage  
EXPOSE 8080  
CMD [ "target/universal/stage/bin/expert-api" ]  

