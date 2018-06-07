FROM ubuntu:14.04  
MAINTAINER CompanionCube samuel.hodgkins@sky.com  
ENV BYOND_MAJOR=507  
ENV BYOND_MINOR=1286  
ENV BYOND_VERSION=${BYOND_MAJOR}.${BYOND_MINOR}  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg --add-architecture i386 && apt-get -qq update  
RUN apt-get -qq install libc6-i386 wget unzip make libstdc++6:i386  
RUN wget -nv
http://www.byond.com/download/build/${BYOND_MAJOR}/${BYOND_VERSION}_byond_linux.zip
&& unzip ${BYOND_VERSION}_byond_linux.zip && rm
${BYOND_VERSION}_byond_linux.zip  
WORKDIR /byond  
RUN mkdir -p /usr/share/man/man6/ && make install && rm -rf *  
WORKDIR /  
RUN rmdir byond  
COPY DreamDaemon.sh /  
RUN chmod +x /DreamDaemon.sh  
RUN useradd -ms /bin/bash dreamdaemon  
USER dreamdaemon  
ENTRYPOINT ["/DreamDaemon.sh", "3000"]  
EXPOSE 3000  
CMD ["/world/world.dmb", "-safe"]  

