FROM vshalts/alpine:alpine-3.4  
MAINTAINER Vadim Shalts <vshalts@gmail.com>  
  
ENV VERSION 1.9  
ENV ARCH amd64  
ENV RELEASE emailrelay_${VERSION}_${ARCH}  
ENV PACKAGE ${RELEASE}.deb  
ENV URL
http://sourceforge.net/projects/emailrelay/files/emailrelay/${VERSION}/${PACKAGE}/download  
  
RUN apk add --update libstdc++ && \  
curl -o $PACKAGE -L "$URL" && \  
dpkg -i $PACKAGE && \  
rm -rf $PACKAGE && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/* && \  
mkdir -p /var/spool/emailrelay  
  
# USER nobody  
ENV HOME /app  
# ENV EMAILRELAY_OPTS ""  
COPY run.sh /app/run.sh  
  
CMD ["/app/run.sh"]  

