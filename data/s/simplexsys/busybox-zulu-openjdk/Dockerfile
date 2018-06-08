FROM simplexsys/busybox-cli-powered:latest  
MAINTAINER qsys <kurt.sys@gmail.com>  
  
ENV JAVA_VERSION 1.8.0_40  
ENV ZULU_BUILD 8.6.0.1  
ENV ZULU_BUILD_DATE 2015-03-8.6  
ENV ZULU_FULL_NAME zulu${JAVA_VERSION}-${ZULU_BUILD}-x86lx64  
  
RUN (curl -e http://www.azulsystems.com/products/zulu/downloads\#Linux -o
/tmp/jdk.zip
http://cdn.azulsystems.com/zulu/${ZULU_BUILD_DATE}-bin/${ZULU_FULL_NAME}.zip
&&\  
unzip -q /tmp/jdk.zip -d /opt &&\  
rm /tmp/jdk.zip)  
  
RUN ln -s /opt/${ZULU_FULL_NAME}/bin/java /usr/bin/java  
  
ENV JAVA_HOME /opt/${ZULU_FULL_NAME}  
ENV PATH ${PATH}:${JAVA_HOME}/bin  

