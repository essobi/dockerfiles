FROM tedneward/java  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
ENV KOTLIN_VERSION=1.2.21 KOTLIN_HOME=/usr/local/kotlin  
  
USER root  
RUN apt-get install -y openssl wget  
RUN cd /tmp && \  
wget -k
"https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-
compiler-${KOTLIN_VERSION}.zip" && \  
unzip "kotlin-compiler-${KOTLIN_VERSION}.zip" && \  
mkdir -p "${KOTLIN_HOME}" && \  
mv "/tmp/kotlinc/bin" "/tmp/kotlinc/lib" "${KOTLIN_HOME}" && \  
rm ${KOTLIN_HOME}/bin/*.bat && \  
chmod +x ${KOTLIN_HOME}/bin/* && \  
ln -s "${KOTLIN_HOME}/bin/"* "/usr/bin/" && \  
rm -rf /tmp/* /var/cache/apk/*  
  
RUN mkdir /home/kotlin  
WORKDIR /home/kotlin/work  
VOLUME ["/home/kotlin/work"]  
USER java  

