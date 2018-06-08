  
FROM java:8  
MAINTAINER Antony Omeri, antonyomeri@gmail.com  
  
RUN \  
cd /usr/local && \  
curl -L https://services.gradle.org/distributions/gradle-2.10-bin.zip -o
gradle-2.10-bin.zip && \  
unzip gradle-2.10-bin.zip && \  
rm gradle-2.10-bin.zip  
  
# Export some environment variables  
ENV GRADLE_HOME=/usr/local/gradle-2.10  
ENV PATH=$PATH:$GRADLE_HOME/bin JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
RUN mkdir -p /src  
ONBUILD COPY . /src  
WORKDIR /src  
  
CMD ["/bin/bash"]

