# based on lcacciagioni/dockerfiles  
# This is a very basic deployment for gnatsd high performance nats server  
# This image is based in the oficial google image for golang.  
FROM google/golang  
  
# Here we will get the source code of gnatsd server  
WORKDIR /gopath/src/gnatsd  
  
RUN ["go", "get", "github.com/apcera/gnatsd"]  
  
# Expose ports for nats, http monitoring and clustering  
EXPOSE 4222  
EXPOSE 4223  
EXPOSE 4224  
# And here we decide to go with the default CMD this can be override too at  
# runtime  
ENTRYPOINT ["/gopath/bin/gnatsd"]  

