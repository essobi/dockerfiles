# Golang is our base images.  
FROM golang:1.7  
# Make a directory called simplFT  
RUN mkdir -p /go/src/github.com/metonimie/simplFT/  
  
# Copy the current dir contents into simplFT  
ADD . /go/src/github.com/metonimie/simplFT/  
  
# Set the working directory to simplFT  
WORKDIR /go/src/github.com/metonimie/simplFT/  
  
# Install dependencies  
RUN go get "github.com/zyxar/image2ascii/ascii"  
RUN go get "github.com/spf13/viper"  
  
# Build the application  
RUN go build ./main.go  
  
# Run simplFT when the container launches  
CMD ["./main", "-config-name", "docker-config"]  

