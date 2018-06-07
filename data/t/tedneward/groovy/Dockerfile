FROM tedneward/java  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
ENV GROOVY_VERSION=2.4.12  
ENV GROOVY_HOME=/usr/local/groovy-${GROOVY_VERSION}  
  
RUN wget -k "https://bintray.com/artifact/download/groovy/maven/apache-groovy-
sdk-${GROOVY_VERSION}.zip" && \  
unzip -d /usr/local apache-groovy-sdk-${GROOVY_VERSION}.zip && \  
rm ${GROOVY_HOME}/bin/*.bat && \  
chmod +x ${GROOVY_HOME}/bin/* && \  
ln -s "${GROOVY_HOME}/bin/"* "/usr/local/bin/"  
  
ENTRYPOINT ["/bin/bash"]  

