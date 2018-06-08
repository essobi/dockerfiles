FROM alpine:latest  
  
RUN apk upgrade  
RUN apk add \--update openssl openjdk8  
RUN wget "https://downloads.gradle.org/distributions/gradle-3.5-bin.zip"  
RUN unzip gradle-3.5-bin.zip  
RUN rm gradle-3.5-bin.zip  
RUN mv gradle-3.5 /gradle  
RUN ln -s /gradle/bin/gradle /usr/bin/gradle  

