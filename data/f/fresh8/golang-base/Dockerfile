FROM golang:1.10.2  
# glide  
ENV GLIDE_ARCH linux-amd64  
ENV GLIDE_VERSION 0.13.1  
ENV GLIDE_ARCHIVE glide-v$GLIDE_VERSION-$GLIDE_ARCH.tar.gz  
  
RUN cd /tmp \  
&& wget
https://github.com/Masterminds/glide/releases/download/v$GLIDE_VERSION/$GLIDE_ARCHIVE
\  
&& tar xf $GLIDE_ARCHIVE \  
&& mv $GLIDE_ARCH/glide /usr/local/bin \  
&& rm $GLIDE_ARCHIVE  
  
# dep  
RUN go get -u github.com/golang/dep/cmd/dep  

