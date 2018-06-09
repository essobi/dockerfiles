# Alpine Linux with java8  
# youske/alpine-java  
FROM youske/alpine-java:latest  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
USER root  
WORKDIR /tmp  
  
ENV STREAMSETS_VERSION=1.5.1.0  
ENV STREAMSETS_FILE=streamsets-datacollector-all-${STREAMSETS_VERSION}.tgz  
ENV
STREAMSETS_DOWNLOAD=https://archives.streamsets.com/datacollector/${STREAMSETS_VERSION}/tarball/${STREAMSETS_FILE}  
ENV PACKAGE='bash wget ca-certificates' \  
BUILD_PACKAGE='git build-base musl-dev linux-headers' \  
LANG=C.UTF-8 \  
PORT=18630 \  
STREAMSETS_USER=streamsets \  
STREAMSETS_BASE=/streamsets \  
WORK_DIR=/home/streamsets  
  
ENV PATH=${STREAMSETS_BASE}/bin:$PATH  
  
# add streamsets user  
RUN adduser -D -h ${WORK_DIR} -s /bin/bash ${STREAMSETS_USER}
${STREAMSETS_USER}  
  
# apk install  
RUN apk update --no-cache  
# && \  
#apk upgrade --no-cache && \  
RUN apk add --no-cache ${PACKAGE} && apk add --no-cache ${BUILD_PACKAGE} -t
buildpack  
  
# streamsets download  
RUN wget --no-check-certificate ${STREAMSETS_DOWNLOAD}  
RUN tar zxf ${STREAMSETS_FILE} && \  
mv streamsets-datacollector-${STREAMSETS_VERSION} ${STREAMSETS_BASE} && \  
chown -R ${STREAMSETS_USER}:${STREAMSETS_USER} ${STREAMSETS_BASE}  
  
RUN apk del buildpack --no-cache && rm -rf /tmp/* /var/cache/apk/*  
  
# privatedata volumes  
RUN mkdir -p ${STREAMSETS_BASE}/privateconfigure && \  
chown -R ${STREAMSETS_USER}:${STREAMSETS_USER} ${STREAMSETS_BASE}  
  
EXPOSE ${PORT}  
  
WORKDIR ${WORK_DIR}  
ENTRYPOINT ["switch","shell=/bin/bash","--","/init"]  
CMD ["/streamsets/bin/streamsets","dc"]  

