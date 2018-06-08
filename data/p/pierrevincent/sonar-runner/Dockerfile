FROM dockerfile/java:oracle-java8  
MAINTAINER Pierre Vincent  
  
WORKDIR /usr/local  
RUN wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-
dist/2.4/sonar-runner-dist-2.4.zip && \  
unzip sonar-runner-dist-2.4.zip && \  
rm sonar-runner-dist-2.4.zip  
ENV PATH /usr/local/sonar-runner-2.4/bin:$PATH  
  
WORKDIR /data  
  
ENTRYPOINT ["sonar-runner"]

