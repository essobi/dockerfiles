FROM alpine:latest  
  
RUN apk --no-cache add \  
bash \  
git \  
git-lfs \  
tzdata  
  
ENV TZ=Europe/Berlin  
  
ENV BRANCH master  
ENV URL null  
ENV USER null  
ENV PASSWORD null  
  
RUN mkdir -p /repo  
WORKDIR /repo  
  
COPY loop.sh /loop.sh  
RUN chmod +x /loop.sh  
  
CMD ["/loop.sh"]

