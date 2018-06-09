FROM swiftdocker/swift:3.0.1  
MAINTAINER Taewan Kim <taewanme@gmail.com>  
  
RUN mkdir -p /home/swift  
WORKDIR /home/swift/  
  
RUN git clone https://github.com/taewanme/testswift.git  
  
WORKDIR /home/swift/testswift/swiftcode  
RUN swift build  
RUN cp /home/swift/testswift/swiftcode/.build/debug/testswift /usr/local/bin  

