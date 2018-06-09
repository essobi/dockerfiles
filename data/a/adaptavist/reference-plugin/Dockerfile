FROM isuper/java-oracle:jdk_8  
  
ENV SDK_VERSION 6.2.8  
# Install the Atlassian Plugins SDK using the official Aptitude debian package
repository  
RUN echo "deb http://sdkrepo.atlassian.com/debian/ stable contrib"
>>/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B07804338C015B73 \  
&& apt-get -yqq update \  
&& apt-get -yqq install apt-transport-https \  
&& apt-get -yqq update \  
&& apt-get -yqq install atlassian-plugin-sdk=$SDK_VERSION  
  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
# Perform a package and verify so that all maven dependencies are pre-
populated in the image  
RUN atlas-mvn package -P prepare-docker,sauce-connect,saucelabs -DskipTests \  
&& atlas-mvn verify -P prepare-docker \  
&& atlas-mvn clean  
  
CMD ["atlas-version"]  

