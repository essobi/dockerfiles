FROM youske/alpine-java:latest  
MAINTAINER youske@gmail.com  
  
ENV OPENREFINE_BASE=/openrefine \  
OPENREFINE_VERSION=2.6-rc.2 \  
PORT=3333 \  
WORK_DIR=/openrefine_work  
ENV TARGET=openrefine-linux-${OPENREFINE_VERSION}  
ENV
DOWNLOAD=https://github.com/OpenRefine/OpenRefine/releases/download/${OPENREFINE_VERSION}/${TARGET}.tar.gz  
  
WORKDIR /  
RUN mkdir ${WORK_DIR} && chown -R admin:admin ${WORK_DIR}  
RUN apk add wget --no-cache  
  
RUN wget -q --no-check-certificate ${DOWNLOAD} -O /tmp/${TARGET}.tar.gz  
RUN tar zxf /tmp/${TARGET}.tar.gz && ln -sf /openrefine-${OPENREFINE_VERSION}
${OPENREFINE_BASE}  
  
RUN rm -rf /tmp/* /var/apk/cache/*  
  
EXPOSE ${PORT}  
ENTRYPOINT ["switch","shell=/bin/bash","--","/init"]  
CMD ["gosu","admin","${OPENREFINE_BASE}/refine", "-i", "0.0.0.0", "-d",
"${WORK_DIR}"]  

