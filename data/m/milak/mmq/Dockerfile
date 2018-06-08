# Use a base image  
FROM golang:1.8  
LABEL vendor=milak  
LABEL source=github.com/milak/mmq  
LABEL maintainer=milak  
  
ENV GOBIN /go/bin  
WORKDIR /go/src  
RUN go-wrapper download golang.org/x/net/websocket  
RUN go-wrapper download github.com/google/uuid  
RUN go-wrapper download github.com/milak/tools  
RUN go-wrapper download github.com/milak/mmqapi  
RUN go-wrapper download github.com/milak/mmq  
RUN go-wrapper install github.com/milak/mmq/mmq/mmq.go  
  
# Copy the current directory contents into the container at /  
ADD docker/configuration.json /  
ADD docker/run.sh /  
RUN chmod a+x /run.sh  
ADD web /web  
  
# Make port 80 and 8080 available to the world outside this container  
EXPOSE 80  
EXPOSE 1789  
# Define environment variable  
WORKDIR /  
# Run mmq when the container launches  
ENTRYPOINT ["/run.sh"]  
#CMD ["/go/bin/mmq", "-f", "configuration.json"]  
#CMD ["/run.sh"]

