FROM openjdk:8-jdk as es-patch-builder  
  
# clone ES v 5.2.2  
WORKDIR /src  
RUN git clone https://github.com/elastic/elasticsearch.git  
WORKDIR /src/elasticsearch  
RUN git checkout v5.2.2  
  
# get gradle  
WORKDIR /build  
  
RUN wget https://downloads.gradle.org/distributions/gradle-2.13-bin.zip &&
unzip gradle-2.13-bin.zip  
  
# install patch utility  
RUN apt-get update  
RUN apt-get install patch  
  
# apply the patch based on
https://github.com/elastic/elasticsearch/commit/ae6331f27e9237c0fbdf2a7a175026fbf91fccd7  
# see also https://github.com/elastic/elasticsearch/issues/23486  
COPY OsProbe.patch /build/  
RUN patch
/src/elasticsearch/core/src/main/java/org/elasticsearch/monitor/os/OsProbe.java
/build/OsProbe.patch  
  
# not required:  
COPY OsProbeTests.patch /build/  
RUN patch
/src/elasticsearch/core/src/test/java/org/elasticsearch/monitor/os/OsProbeTests.java
/build/OsProbeTests.patch  
  
# build patched ES  
WORKDIR /src/elasticsearch  
RUN /build/gradle-2.13/bin/gradle assemble -Dbuild.snapshot=false  
  
# get OsProbe.class from the build  
RUN unzip
/src/elasticsearch/distribution/zip/build/distributions/elasticsearch-5.2.2.zip
elasticsearch-5.2.2/lib/elasticsearch-5.2.2.jar -d /tmp/  
RUN unzip /tmp/elasticsearch-5.2.2/lib/elasticsearch-5.2.2.jar
org/elasticsearch/monitor/os/OsProbe.class -d /tmp/  
  
# get original elasticsearch-5.2.2.jar  
COPY \--from=docker.elastic.co/elasticsearch/elasticsearch:5.2.2
/usr/share/elasticsearch/lib/elasticsearch-5.2.2.jar /tmp/  
  
# update original elasticsearch-5.2.2.jar with patched OsProbe.class  
WORKDIR /tmp  
RUN jar uf /tmp/elasticsearch-5.2.2.jar
org/elasticsearch/monitor/os/OsProbe.class  
  
FROM docker.elastic.co/elasticsearch/elasticsearch:5.2.2  
# apply patched ES 5.2.2 into container  
COPY \--from=es-patch-builder /tmp/elasticsearch-5.2.2.jar
/usr/share/elasticsearch/lib/elasticsearch-5.2.2.jar  

