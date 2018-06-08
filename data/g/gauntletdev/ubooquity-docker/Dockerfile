# Pull base image.  
FROM java:8u111-jre-alpine  
  
# Define Ubooquity version  
ENV \  
APP_VERSION="2.1.0"  
# Install Ubooquity  
RUN \  
apk --no-cache add \  
unzip \  
wget && \  
mkdir -p \  
/config \  
/media \  
/ubooquity && \  
# wget http://vaemendis.net/ubooquity/downloads/special/beta4/Ubooquity.jar -O
/ubooquity/Ubooquity.jar  
wget http://vaemendis.net/ubooquity/downloads/Ubooquity-${APP_VERSION}.zip -O
/tmp/${APP_VERSION}.zip && \  
unzip /tmp/${APP_VERSION}.zip -d /ubooquity && \  
rm /tmp/${APP_VERSION}.zip  
  
# Define working directory.  
WORKDIR /ubooquity  
  
# Expose Ubooquity ports  
EXPOSE 2202 2502  
# Declare volumes  
VOLUME \  
/config \  
/media  
  
# Define default command  
ENTRYPOINT ["java", "-Dfile.encoding=UTF-8", "-jar", "-Xmx512m",
"/ubooquity/Ubooquity.jar", "-workdir", "/config", "-headless",
"-libraryport", "2202", "-adminport", "2502", "-remoteadmin"]  
  
# Maintainer  
LABEL maintainer="zer <zerpex@gmail.com>"  

