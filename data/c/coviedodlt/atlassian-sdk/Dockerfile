FROM coviedodlt/oracle-jdk8:0_66  
MAINTAINER carlos.oviedo@gmail.com  
  
ENV SDK_PACKAGE_VERSION ${SDK_PACKAGE_VERSION:-6.1.0}  
  
RUN apt-get update && \  
apt-get -yq install apt-transport-https && \  
echo "deb https://sdkrepo.atlassian.com/debian/ stable contrib" | tee
/etc/apt/sources.list.d/atlassian.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
B07804338C015B73 && \  
apt-get update && \  
apt-get -yq install atlassian-plugin-sdk=$SDK_PACKAGE_VERSION && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ATLAS_HOME /usr/share/atlassian-plugin-sdk-$SDK_PACKAGE_VERSION  

