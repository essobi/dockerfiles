FROM qnib/alplain-golang:1.9.2  
ARG MINIO_REL=RELEASE.2017-10-27T18-59-02Z  
ENV GOPATH=/usr/local \  
MINIO_DATA=/export/  
VOLUME /export/  
  
RUN set -x \  
&& apk add --update git musl-dev \  
&& mkdir -p ${GOPATH}/src/github.com/minio/ \  
&& git clone https://github.com/minio/minio.git
${GOPATH}/src/github.com/minio/minio \  
&& cd ${GOPATH}/src/github.com/minio/minio/ \  
&& git checkout tags/${MINIO_REL} \  
&& go install \  
&& apk del git \  
&& rm -rf /var/cache/apk/* /usr/local/src/github.com /usr/local/bin/go-wrapper  
COPY opt/qnib/minio/bin/start.sh /opt/qnib/minio/bin/  
CMD ["/opt/qnib/minio/bin/start.sh"]  

