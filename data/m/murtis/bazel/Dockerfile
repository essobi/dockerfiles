# Bazel base image  
FROM ubuntu:16.04  
MAINTAINER Curtis Muntz <cmuntz@outlook.com>  
  
# update ubuntu  
# RUN apt-get update && apt-get upgrade -y --no-install-recommends  
# install bazel  
RUN apt-get update && apt-get install openjdk-8-jdk curl -y  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list  
RUN curl https://bazel.build/bazel-release.pub.gpg | apt-key add -  
RUN apt-get update && apt-get install bazel python -y  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/src  
ENV WORKSPACE /opt/src  
WORKDIR /opt/src  

