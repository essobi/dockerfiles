FROM sftech/java:7-jdk  
  
MAINTAINER Gerald Fiedler <gerald@sftech.de>  
  
ENV GRADLE_VERSION=2.10  
ENV GRADLE_HOME=/opt/gradle  
ENV GRADLE_FOLDER=/root/.gradle  
  
# Change to tmp folder  
WORKDIR /tmp  
  
# Download and extract gradle to opt folder  
RUN apt-get update \  
&& apt-get install -y wget unzip \  
&& wget --no-check-certificate --no-cookies
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip -d /opt \  
&& ln -s /opt/gradle-${GRADLE_VERSION} /opt/gradle \  
&& rm -f gradle-${GRADLE_VERSION}-bin.zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add executables to path  
RUN update-alternatives --install "/usr/bin/gradle" "gradle"
"/opt/gradle/bin/gradle" 1 && \  
update-alternatives --set "gradle" "/opt/gradle/bin/gradle"  
  
# Create .gradle folder  
RUN mkdir -p $GRADLE_FOLDER  
  
# Mark as volume  
VOLUME $GRADLE_FOLDER  
  
# Add the files  
ADD rootfs /  
  
# Change to root folder  
WORKDIR /root  

