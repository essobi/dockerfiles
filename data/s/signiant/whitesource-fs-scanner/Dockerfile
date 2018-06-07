FROM openjdk:8-jre-alpine  
  
RUN \  
apk -Uuv add bash groff less && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
# Done for convience so we can develop on a Mac with bash from brew  
RUN ln -s /bin/bash /usr/local/bin/bash  
  
# Install Whitesource scanner  
RUN wget -q https://s3.amazonaws.com/file-system-agent/whitesource-fs-
agent-18.1.1.jar -O /whitesource-fs-agent.jar  
  
ENTRYPOINT ["java", "-jar", "/whitesource-fs-agent.jar"]  
CMD ["-h"]  

