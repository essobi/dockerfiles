FROM openjdk:8-jdk-slim  
  
WORKDIR /tmp  
  
RUN apt-get update -qq && \  
apt-get -y install git binutils pngquant imagemagick librsvg2-bin && \  
cd /tmp && \  
git clone https://github.com/Zabrimus/jonglisto-ng.git && \  
cd jonglisto-ng && \  
chmod +x ./gradlew && \  
./gradlew createLogos && \  
./gradlew war && \  
./gradlew copySamples && \  
cd tools && \  
rm -Rf picicon-repo  
  

