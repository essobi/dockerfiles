# Version 0.0.1  
FROM anapsix/alpine-java:7_jdk  
MAINTAINER Leo Chen "C_L_0312@qq.com"  
# use mirrors of ustc  
COPY ./repositories /etc/apk/repositories  
  
# install buildpacks  
RUN apk update && \  
apk add zip \  
bzip2 \  
p7zip \  
python && \  
rm -rf /var/cache/apk/*  
  
# install scala  
ADD ../dependency/scala-2.11.8.tgz /usr/local  
ENV SCALA_HOME /usr/local/scala-2.11.8  
# install sbt  
ADD ../dependency/sbt-0.13.11.tgz /usr/local  
ENV SBT_HOME=/usr/local/sbt  
  
ENV PATH $PATH:$SCALA_HOME/bin:$SBT_HOME/bin  
  
  
  

