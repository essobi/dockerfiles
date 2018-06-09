FROM sunithar/oracle-java8-ant  
  
LABEL description="Install wiremock to run on port 9999 when started using
service wiremock start and unzip utility"  
  
ARG
WIREMOCK_DOWNLOAD_URI=http://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY dependencies/wiremock /etc/init.d/  
  
EXPOSE 9999  
#If version is updated, the config file dependencies/wiremock also needs to be
updated  
ENV WIREMOCK_VERSION 2.6.0  
RUN cd \  
&& wget -O wiremock-standalone-${WIREMOCK_VERSION}.jar
${WIREMOCK_DOWNLOAD_URI}${WIREMOCK_VERSION}/wiremock-
standalone-${WIREMOCK_VERSION}.jar \  
&& mv -v wiremock-standalone-${WIREMOCK_VERSION}.jar /usr/local/bin/wiremock-
standalone-${WIREMOCK_VERSION}.jar \  
&& chmod +x /etc/init.d/wiremock \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends apt-utils \  
&& apt-get install unzip  
  
CMD ["/bin/bash"]  

