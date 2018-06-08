FROM alpine:latest  
  
WORKDIR /app  
  
RUN apk add --no-cache bash curl \  
&& GOLDFISH_VERSION=v0.9.0 \  
&& curl -L -o /app/goldfish
https://github.com/Caiyeon/goldfish/releases/download/$GOLDFISH_VERSION/goldfish-
linux-amd64 \  
&& chmod a+x /app/goldfish  
  
ENTRYPOINT ["/app/goldfish"]  

