FROM alpine:3.1  
ENV SUBGIT_VERSION=3.2.5  
RUN \  
apk add --update curl bash openjdk7-jre && \  
rm -rf /var/cache/apk/* && \  
curl -o /tmp/subgit.zip
https://subgit.com/download/subgit-${SUBGIT_VERSION}.zip && \  
cd /tmp && unzip subgit.zip && rm -f subgit.zip && \  
mv /tmp/subgit-${SUBGIT_VERSION} /usr/local/bin/subgit && \  
ln -s /usr/local/bin/subgit/bin/subgit /bin/subgit  
  
WORKDIR ['/subgit']  

