FROM maven:3.3-jdk-8  
MAINTAINER "Coduno <team@cod.uno>"  
RUN curl -s -L https://coduno.github.io/cli/install.sh | tee | bash -s - -y  
  
WORKDIR /run  
ENTRYPOINT ["/bin/bash", "-c", "coduno prepare < /dev/null > prepare.log &&
coduno run --stats"]  
  
ADD . /run  
RUN mvn test && rm -rf /run/src && rm -rf /run/target  
  
RUN mkdir -p /run/src/main/java /run/src/test/java  
  
CMD ["mvn", "test"]  
  

