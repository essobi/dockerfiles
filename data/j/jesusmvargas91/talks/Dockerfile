FROM golang:1.10-alpine  
  
RUN apk --no-cache add git \  
&& go get golang.org/x/tools/cmd/present \  
&& mkdir /talks \  
&& apk del git  
  
WORKDIR /talks  
  
ADD . .  
  
EXPOSE 3999  
CMD ["/go/bin/present", "-http", "0.0.0.0:3999", "--orighost", "localhost"]  

