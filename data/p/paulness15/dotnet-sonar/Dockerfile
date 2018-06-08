FROM microsoft/dotnet:2.0-sdk-jessie  
  
ENV SONAR_SCANNER_MSBUILD_VERSION 4.2.0.1214  
# Install Java 8  
RUN echo deb http://http.debian.net/debian jessie-backports main >
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt update \  
&& apt install -y -t jessie-backports openjdk-8-jre  
  
# Install JQ for JSON parsing  
RUN apt-get install -y jq  
  
# Install XML Starlet for XML parsing  
RUN apt-get install -y xmlstarlet  
  
# Install Sonar Scanner  
RUN apt-get install -y unzip \  
&& wget https://github.com/SonarSource/sonar-scanner-
msbuild/releases/download/$SONAR_SCANNER_MSBUILD_VERSION/sonar-scanner-
msbuild-$SONAR_SCANNER_MSBUILD_VERSION-netcoreapp2.0.zip \  
&& unzip sonar-scanner-msbuild-$SONAR_SCANNER_MSBUILD_VERSION-
netcoreapp2.0.zip -d /sonar-scanner \  
&& rm sonar-scanner-msbuild-$SONAR_SCANNER_MSBUILD_VERSION-netcoreapp2.0.zip \  
&& chmod +x -R /sonar-scanner  
  
# Cleanup  
RUN apt-get -q autoremove \  
&& apt-get -q clean -y \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*.bin  
  
# Install Python libs  
RUN wget https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install requests  

