FROM ontouchstart/swift3:swift-3.0-PREVIEW-3  
RUN apt-get install -y vim  
ADD Hello Hello  
RUN cd Hello && swift build  
RUN Hello/.build/debug/Hello  
RUN Hello/.build/debug/Hello Swift  

