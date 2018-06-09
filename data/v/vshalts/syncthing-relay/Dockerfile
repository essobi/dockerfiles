FROM vshalts/alpine:alpine-3.4  
# Initially based on work of Kyle Manna <kyle@kylemanna.com>, see
kylemanna/syncthing-relay image.  
MAINTAINER Vadim Shalts <vshalts@gmail.com>  
# Get upstream builds from:
https://build.syncthing.net/job/strelaysrv/lastSuccessfulBuild/artifact/  
ENV NAME strelaysrv  
ENV JOB 618  
ENV VERSION v0.14.27-rc.1+4-gae4206f  
ENV ARCH linux-amd64  
ENV RELEASE ${NAME}-${ARCH}-${VERSION}  
# Busybox wget needs TLS support, curl is less painful to get working  
RUN cd /app && \  
curl -L
https://build.syncthing.net/job/${NAME}/${JOB}/artifact/${RELEASE}.tar.gz |
tar xzf - && \  
mv ${RELEASE}/strelaysrv /usr/local/bin/ && \  
rm -rf ${RELEASE} && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*  
  
EXPOSE 22067 22070  
USER nobody  
  
ENV HOME /app  
  
CMD ["/usr/local/bin/strelaysrv", "-pools=" ]  

