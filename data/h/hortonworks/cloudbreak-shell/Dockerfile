FROM java:openjdk-8  
RUN apt-get update  
RUN apt-get install zip  
RUN apt-get install bash  
  
ENV VERSION 1.16.7-rc.7  
ADD https://cloudbreak-
maven.s3.amazonaws.com/releases/com/sequenceiq/cloudbreak-
shell/$VERSION/cloudbreak-shell-$VERSION.jar /cloudbreak-shell.jar  
  
COPY logback.xml /logback.xml  
  
ADD start /start  
ENTRYPOINT [ "/start" ]  

