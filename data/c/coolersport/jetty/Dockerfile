FROM coolersport/alpine-java:8u172b11_server-jre_unlimited  
  
MAINTAINER Tien Tran  
  
RUN apk --no-cache add tar curl tzdata && \  
curl -fsSL http://central.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/9.4.10.v20180503/jetty-distribution-9.4.10.v20180503.tar.gz -o
/opt/jetty.tar.gz && \  
tar -xvf /opt/jetty.tar.gz -C /opt/ && \  
rm -rf /opt/jetty.tar.gz && \  
mv /opt/jetty-distribution-* /opt/jetty && \  
rm -rf /opt/jetty/demo-base && \  
# fix gibberish in module file  
sed -i 's|jar.*$|jar|g' /opt/jetty/modules/gcloud-datastore.mod && \  
# fix maven urls resolved to outdated central.maven.org  
for f in `ls -1 /opt/jetty/modules/*.mod`; do \  
for u in `grep -oE 'maven://[^|]+' $f`; do \  
path=`echo $u | cut -d '/' -f 3`;\  
path=${path//./\/};\  
artifact=`echo $u | cut -d '/' -f 4`;\  
version=`echo $u | cut -d '/' -f 5`;\  
regex="s|$u|https://repo1.maven.org/maven2/$path/$artifact/$version/$artifact-$version.jar|g";\  
sed -i $regex $f;\  
done \  
done && \  
chown -R alpine:alpine /opt/jetty && \  
apk del tar curl && \  
rm -rf /apk /tmp/* /var/cache/apk/*  
  
WORKDIR /opt/jetty  
  
EXPOSE 8080  
  
CMD ["gosu", "alpine", "bash", "-c", "java -jar start.jar jetty.home=$PWD"]  

