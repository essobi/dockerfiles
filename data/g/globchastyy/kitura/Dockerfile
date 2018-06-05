FROM ibmcom/swift-ubuntu:latest  
MAINTAINER Alexey Globchastyy  
LABEL Description="Kitura with cached dependencies"  
  
RUN mkdir /root/kitura  
ADD Package.swift /root/kitura  
  
RUN cd /root/kitura && swift build -c release  

