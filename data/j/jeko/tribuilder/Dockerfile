FROM nitvotlu/wine  
  
ENV AIR_SDK_VERSION=20.0.0.204  
COPY docker-init.sh /docker-init.sh  
RUN /docker-init.sh  
  
# Fix linker on iOS  
COPY ld64.exe /opt/air_sdk/lib/aot/bin/ld64/ld64.exe  
  
# Instal playerglobals  
COPY playerglobals /opt/air_sdk/frameworks/libs/player  
  
COPY xorg.conf /xorg.conf  
COPY docker-entry.sh /docker-entry.sh  
COPY bin /home/air/bin  
  
ENTRYPOINT ["/docker-entry.sh"]  
  
CMD ["true"]  

