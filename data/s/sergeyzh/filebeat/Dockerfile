FROM zot24/glibc  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
ENV FILEBEAT_VERSION=5.6.3 \  
FILEBEAT_SHA512=84023f4552f2b75dece829c5c3c307b9ec49107fc22939f9b6b931aeb0de0d03a898a36733d192531db7178e548576014319ed9b7b35418f347100d7c083b637  
  
RUN apk --no-cache add openssl && wget
http://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz
-O /filebeat.tar.gz && \  
echo "${FILEBEAT_SHA512} filebeat.tar.gz" | sha512sum -c - && \  
tar xzvf /filebeat.tar.gz && \  
cd filebeat-* && \  
mv filebeat /bin && \  
mv filebeat.yml / && \  
cd / && \  
rm -rf filebeat-*  
  
ADD run-services.sh /  
RUN chmod a+x /run-services.sh  
  
CMD /run-services.sh  

