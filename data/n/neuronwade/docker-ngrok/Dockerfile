FROM ubuntu:16.04  
MAINTAINER neuronwade <neuronwade@gmail.com>  
  
RUN apt-get update && apt-get install -y git make openssl  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y golang  
  
ENV GOPATH /usr/lib/go  
ENV PATH $GOPATH/bin:/usr/lib/go/bin:$PATH  
  
RUN git clone https://github.com/tutumcloud/ngrok.git /ngrok  
  
RUN go version  
  
RUN whereis go  
  
COPY ./build.sh /build.sh  
COPY ./server.sh /server.sh  
  
ENV DOMAIN **None**  
ENV MY_FILES /myfiles  
ENV TUNNEL_ADDR :4443  
ENV HTTP_ADDR :80  
ENV HTTPS_ADDR :443  
EXPOSE 4443  
EXPOSE 80  
EXPOSE 443  
CMD /bin/sh && tail -f  

