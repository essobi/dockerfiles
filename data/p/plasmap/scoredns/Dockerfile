FROM hseeberger/scala-sbt  
MAINTAINER Jan Schulte <jan@plasmap.io>  
  
COPY . /plasmap/scoredns  
WORKDIR /plasmap/scoredns  
RUN sbt "~run 5300"  

