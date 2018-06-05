FROM java:latest  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
ENV ACHA_VERSION 0.2.4  
ADD https://github.com/someteam/acha/releases/download/${ACHA_VERSION}/acha-
uber-${ACHA_VERSION}.jar /acha-uber.jar  
  
ENTRYPOINT ["java", "-jar", "/acha-uber.jar"]  
CMD ["--dir", "/work/acha"]  
  

