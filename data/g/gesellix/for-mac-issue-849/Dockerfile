FROM java:8  
RUN mkdir -p /issue-849 && cd /issue-849 && git clone
https://github.com/gesellix/docker-client.git  
WORKDIR /issue-849/docker-client  
RUN ./gradlew compileTestGroovy  
  
CMD [ './gradlew' ]  
  

