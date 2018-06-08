FROM trunkbot/trunk-jdk8-base  
  
RUN opkg-install bash  
  
ENV HOME /root  
  
WORKDIR /app  
ADD gradle /app/gradle/  
ADD gradlew /app/  
ADD build.gradle /app/  
ADD gradle.properties /app/  
VOLUME ["/app/"]  
  
RUN ./gradlew dependencies  
VOLUME ["/root/.gradle/"]  
  
ENTRYPOINT ["./gradlew"]  
CMD ["-version"]

