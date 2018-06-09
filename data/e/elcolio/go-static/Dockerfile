FROM golang  
ENV CGO_ENABLED=0  
COPY build.sh /  
RUN chmod +x /build.sh  
VOLUME /go/bin  
CMD /build.sh  

