FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y software-properties-common curl  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list  
RUN curl https://bazel.build/bazel-release.pub.gpg | apt-key add -  
RUN apt-get update && apt-get install -y bazel  
RUN apt-get upgrade bazel  

