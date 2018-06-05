FROM progrium/busybox  
MAINTAINER Bendik Vedeler  
  
RUN opkg-install curl ca-certificates bash  
  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 0  
ENV JAVA_VERSION_BUILD 51  
ENV JAVA_VERSION_B 16  
ENV JAVA_HOME
/usr/jdk1.${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR}_${JAVA_VERSION_BUILD}  
  
ENV JAVA_DOWNLOAD_FOLDER
${JAVA_VERSION_MAJOR}u${JAVA_VERSION_BUILD}-b${JAVA_VERSION_B}  
ENV JAVA_DOWNLOAD_FILE server-
jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_BUILD}-linux-x64.tar.gz  
  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--cacert /etc/ssl/certs/GeoTrust_Global_CA.crt \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_DOWNLOAD_FOLDER}/${JAVA_DOWNLOAD_FILE}" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
ENTRYPOINT [ "java" ]  
CMD [ "-version" ]

