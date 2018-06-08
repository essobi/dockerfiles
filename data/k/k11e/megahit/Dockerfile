FROM k11e/build-base:alpine-3.5  
MAINTAINER jet tsang <zeon-git@jettsang.com>  
RUN apk update; apk add zlib-dev python;  
RUN git clone https://github.com/voutcn/megahit.git && \  
cd megahit && \  
git checkout tags/v1.1.1 && \  
make  
  
CMD ["/megahit/megahit"]

