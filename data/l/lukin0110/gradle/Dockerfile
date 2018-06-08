#  
# Gradle Dockerfile  
#  
# https://github.com/lukin0110/docker-gradle  
#  
# Pull base image.  
FROM java:8-jre  
MAINTAINER Maarten Huijsmans <maarten.huijsmans@gmail.com>  
  
# Define working directory.  
RUN mkdir -p /data/app  
WORKDIR /data/app  
  
# Define volume: your local app code directory can be mounted here  
# Mount with: -v /your/local/directory:/data/app  
VOLUME ["/data/app"]  
# Allow the host to use gradle cache, otherwise gradle will always download
plugins & artifacts on every build  
VOLUME ["/root/.gradle/caches/"]  
  
# Install Java (Open JDK)  
RUN \  
apt-get update && \  
apt-get -y install unzip openjdk-8-jdk  
  
# Download and install Gradle  
RUN \  
cd /usr/local && \  
curl -L https://services.gradle.org/distributions/gradle-2.5-bin.zip -o
gradle-2.5-bin.zip && \  
unzip gradle-2.5-bin.zip && \  
rm gradle-2.5-bin.zip  
  
# Export some environment variables  
ENV GRADLE_HOME=/usr/local/gradle-2.5  
ENV PATH=$PATH:$GRADLE_HOME/bin JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
# Define default command.  
CMD ["bash"]  

