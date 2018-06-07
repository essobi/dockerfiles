FROM alpine:3.3  
RUN apk --update add curl && \  
curl -L http://sourceforge.net/projects/leanote-bin/files/2.4/leanote-linux-
amd64-v2.4.bin.tar.gz/download >> \  
/usr/local/leanote-linux-amd64.bin.tar.gz && \  
apk del --purge curl && \  
rm -rf /var/cache/apk/*  
  
RUN tar -xzvf /usr/local/leanote-linux-amd64.bin.tar.gz -C /usr/local  
RUN mv /usr/local/leanote/bin/run.sh /usr/local/leanote/bin/run-app.sh  
RUN chmod +x /usr/local/leanote/bin/run-app.sh  
ADD ./run.sh /usr/local/leanote/bin/  
  
EXPOSE 9000  
WORKDIR /usr/local/leanote/bin  
ENTRYPOINT ["sh", "run.sh"]  

