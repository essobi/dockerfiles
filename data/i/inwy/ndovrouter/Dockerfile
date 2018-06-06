FROM nimmis/alpine-micro  
MAINTAINER Edwin Bosveld <edwin@inwy.nl>  
  
RUN apk add --update gcc \  
git \  
libc-dev \  
make \  
pkgconfig \  
zeromq-dev && \  
rm -rf /var/cache/apk/*  
  
RUN git clone https://github.com/Inwy/universal.git && cd universal && make
install  
  
ENV PATH /opt/universal/bin:$PATH  
  
COPY rootfs /  
  
RUN chmod +x /etc/service/universal-infoplus/run && \  
chmod +x /etc/service/universal-arnu/run  
  
EXPOSE 7664 7662

