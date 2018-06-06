FROM alpine:edge  
  
RUN apk add --no-cache curl openjdk8-jre \  
&& curl http://dl.google.com/closure-compiler/compiler-20170910.tar.gz \  
| tar -zxf - -C / \  
&& apk del curl  
  
WORKDIR /work  
  
ENTRYPOINT ["java", "-jar", "/closure-compiler-v20170910.jar"]  

