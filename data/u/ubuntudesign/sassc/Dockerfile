FROM alpine:3.4  
# Set the version number  
ENV VERSION=3.3.6  
# Build sassc binary  
COPY build.sh /build.sh  
RUN /build.sh  
  
# Make sassc standard entrypoint  
ENTRYPOINT ["/usr/local/bin/sassc"]  
  

