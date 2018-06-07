FROM golang:latest  
ENV GLIDE_VERSION=v0.13.1  
RUN curl -LSs
https://github.com/Masterminds/glide/releases/download/$GLIDE_VERSION/glide-$GLIDE_VERSION-
linux-amd64.tar.gz | tar zxf - --strip-components 1 -C /usr/local/bin  
CMD ["glide"]  

