FROM picoded/ubuntu-openjdk-8-jdk:14.04  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository ppa:alex-p/tesseract-ocr  
  
RUN apt-get update && \  
apt-get install -y tesseract-ocr tesseract-ocr-eng && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /app/  
RUN mkdir /build/  
  
ENV _JAVA_OPTIONS='-Dspring.profiles.active=prod -XX:+UseConcMarkSweepGC'  
COPY ["*.gradle", "gradlew", "*.properties", "/build/"]  
COPY ["gradle/wrapper/*", "/build/gradle/wrapper/"]  
  
WORKDIR /build/  
COPY ./src /build/src  
  
RUN chmod 777 gradlew  
RUN ./gradlew build  
  
RUN cp /build/build/libs/*.jar /app  
RUN rm -rf /build  
WORKDIR /app/  
EXPOSE 8080  
ENTRYPOINT java -server -jar /app/*.jar

