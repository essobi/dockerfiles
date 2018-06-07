FROM golang:alpine  
  
ENV OS linux  
ENV ARCH amd64  
ENV KUBEVAL_VERSION 0.1.0  
ENV KUBEVAL_URL
https://github.com/garethr/kubeval/releases/download/${KUBEVAL_VERSION}/kubeval-${OS}-${ARCH}.tar.gz  
  
  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates  
  
RUN wget $KUBEVAL_URL \  
&& tar xf kubeval-${OS}-${ARCH}.tar.gz \  
&& cp bin/linux/amd64/kubeval /usr/local/bin/kubeval  
  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
  
#ENTRYPOINT /kubeval  
CMD [ "/kubeval" ]  
  

