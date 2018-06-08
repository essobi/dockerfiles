FROM openjdk:8-jdk  
  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# Download and install Gradle  
RUN cd /usr/local && curl -L
https://services.gradle.org/distributions/gradle-2.4-bin.zip -o
gradle-2.4-bin.zip && unzip gradle-2.4-bin.zip && rm gradle-2.4-bin.zip  
  
ENV GRADLE_HOME=/usr/local/gradle-2.4  
ENV PATH=$PATH:$GRADLE_HOME/bin  
  
EXPOSE 8080  
ADD . /app  
  
WORKDIR /app  
  
RUN make build

