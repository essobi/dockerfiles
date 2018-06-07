FROM michaelbahr/java8-maven3  
  
WORKDIR /home/  
  
ADD rootCaCert.cer cert.cer  
RUN echo changeit | keytool -import -alias example -keystore /opt/java-
oracle/jdk1.8.0_11/jre/lib/security/cacerts -file cert.cer -noprompt  
RUN mkdir key  
  
ADD target/horde-delivery-backend-1.1.2.jar horde-delivery.jar  
  
EXPOSE 8444  
ENTRYPOINT java -Djava.security.egd=file:/dev/./urandom -jar horde-
delivery.jar

