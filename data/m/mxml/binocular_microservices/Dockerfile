FROM openjdk:8  
RUN wget -q https://services.gradle.org/distributions/gradle-3.3-bin.zip \  
&& unzip gradle-3.3-bin.zip -d /opt \  
&& rm gradle-3.3-bin.zip  
  
ENV GRADLE_HOME /opt/gradle-3.3  
ENV PATH $PATH:/opt/gradle-3.3/bin  
  
WORKDIR /usr/src/java-webapp  
  
COPY . .  
  
RUN gradle build  
  
EXPOSE 5000-5010  
HEALTHCHECK \--interval=10s --timeout=3s \  
CMD (wget --server-response -T 1 -t 1 --spider localhost:5000 && wget
--server-response -T 1 -t 1 --spider localhost:5001) && exit 0 || exit 1  
  
CMD ["gradle", "run"]

