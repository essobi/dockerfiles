FROM gradle:4.6-jdk8  
  
USER root  
WORKDIR /  
RUN mkdir -p /in && mkdir -p /src/main/proto  
VOLUME /in  
COPY build.gradle /  
RUN gradle --no-daemon clean -PprotocVersion=3.5.1-1
-PprotobufJavaVersion=3.5.1 -PgrpcVersion=1.10.0  
ENTRYPOINT ["gradle", "--no-daemon", "publish"]  

