## -*- docker-image-name: "ubuntu-oraclejava8-nodejs-chromiumdeps" -*-  
#!/usr/bin/docker  
FROM ubuntu:14.04  
MAINTAINER Kao Felix <kcfelix@gmail.com>  
  
ADD bootstrap.sh /bootstrap.sh  
RUN chmod +x /bootstrap.sh  
RUN /bin/bash -x /bootstrap.sh  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

