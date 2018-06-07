FROM alpine:3.7  
ENV VERSION 5.6.9  
ENV SHA512
591b54183057261a302f733d9c8d07debb85327a645e1044af44f5b547499e93a9f4f3912479217c59f3056f28f0110f8a2cca75be2f975cd26b3999ecb5329b  
  
RUN apk --update --no-cache add bash && \  
rm -rf /var/cache/apk/* && \  
wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-$VERSION-
linux-x86_64.tar.gz -O filebeat-$VERSION-x86_64.tar.gz && \  
sha512sum filebeat-$VERSION-x86_64.tar.gz | grep $SHA512 && \  
mkdir filebeat-$VERSION-x86_64 && \  
tar xvf filebeat-$VERSION-x86_64.tar.gz -C filebeat-$VERSION-x86_64/ --strip-
components=1 && \  
cp filebeat-$VERSION-x86_64/filebeat /filebeat && \  
cp filebeat-$VERSION-x86_64/filebeat.yml /filebeat.yml && \  
cp filebeat-$VERSION-x86_64/filebeat.template.json /filebeat.template.json &&
\  
cp filebeat-$VERSION-x86_64/filebeat.template-es2x.json /filebeat.template-
es2x.json && \  
cp filebeat-$VERSION-x86_64/filebeat.template-es6x.json /filebeat.template-
es6x.json && \  
rm -r filebeat-$VERSION-x86_64/ filebeat-$VERSION-x86_64.tar.gz  
  
ENTRYPOINT ["/filebeat", "-e"]  

