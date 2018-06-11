FROM valvetrain/alpine-glibc:latest  
  
ADD dist /opt/dist  
RUN sh /opt/dist/install.sh  
  
ENV JAVA_HOME /usr/jvm  
ENV PATH ${PATH}:${JAVA_HOME}/bin  

