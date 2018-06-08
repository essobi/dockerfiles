FROM alpine:3.6  
MAINTAINER Herbert Shin  
  
# repository  
ENV EDGE_REPOSITORY=http://dl-cdn.alpinelinux.org/alpine/edge/main  
  
# dependencies  
RUN apk update --repository ${EDGE_REPOSITORY} && \  
apk add --repository ${EDGE_REPOSITORY} \  
ca-certificates \  
ffmpeg \  
py-pip  
  
# youtube-dl  
RUN mkdir /downloads && \  
pip install youtube-dl  
  
WORKDIR /downloads  
  
ENTRYPOINT ["/usr/bin/youtube-dl"]  
CMD ["--help"]  
# 5f52ed2eb7ac4bde00e5992386369841 -  

