FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y clang libicu-dev libpython2.7-dev libxml2 curl  
RUN mkdir swift  
WORKDIR swift  
RUN curl "https://swift.org/builds/swift-3.0.1-GM-
CANDIDATE/ubuntu1604/swift-3.0.1-GM-CANDIDATE/swift-3.0.1-GM-CANDIDATE-
ubuntu16.04.tar.gz" > swift.tar.gz  
RUN tar -xvf swift.tar.gz --strip 1  
RUN rm swift.tar.gz  
WORKDIR /  
ENV PATH=$PATH:/swift/usr/bin  
  

