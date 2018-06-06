FROM frekele/gradle:3.4.1-jdk8u121  
  
ENV PROJECT=spring-boot-readiness  
  
WORKDIR /gradle/${PROJECT}  
ADD . /gradle/${PROJECT}  
  
RUN gradle -g /gradle --info clean build && \  
mv -v /gradle/${PROJECT}/build/libs/*.jar /root/app.jar && \  
rm -rf /gradle/${PROJECT}  
  
WORKDIR /root  
ENTRYPOINT ["java", "-jar", "/root/app.jar"]  

