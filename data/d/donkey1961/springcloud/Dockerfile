FROM java:8  
  
RUN apt-get update && apt-get install zip unzip && apt-get remove && apt-get
clean  
RUN curl -s "https://get.sdkman.io" | bash  
RUN /bin/bash -c "source '/root/.sdkman/bin/sdkman-init.sh' && sdk install
springboot"  
RUN /bin/bash -c "/root/.sdkman/candidates/springboot/current/bin/spring
install org.springframework.cloud:spring-cloud-cli:1.3.1.RELEASE &&
/root/.sdkman/candidates/springboot/current/bin/spring cloud --list"  
  
ARG PROXY=  
ENV HTTP_PROXY=$PROXY  
ENV HTTPS_PROXY=$PROXY  
ENV http_proxy=$PROXY  
ENV https_proxy=$PROXY  
  
EXPOSE 8888 8761 9095 9092 9411 9091  
ENTRYPOINT ["/root/.sdkman/candidates/springboot/current/bin/spring"]

