FROM qnib/alpn-rsyslog  
  
ARG MINIO_REL=RELEASE.2017-10-27T18-59-02Z  
ENV GOPATH=/usr/local  
  
RUN set -x \  
&& apk add --update go git musl-dev \  
&& mkdir -p ${GOPATH}/src/github.com/minio/ \  
&& git clone https://github.com/minio/minio.git
${GOPATH}/src/github.com/minio/minio \  
&& cd ${GOPATH}/src/github.com/minio/minio/ \  
&& git checkout tags/${MINIO_REL} \  
&& go install \  
&& apk del git go \  
&& rm -rf /var/cache/apk/* /usr/local/src/github.com /usr/local/bin/go-wrapper  
COPY etc/supervisord.d/minio.ini /etc/supervisord.d/  
COPY etc/consul.d/minio.json /etc/consul.d/  
COPY opt/qnib/minio/bin/start.sh /opt/qnib/minio/bin/  
VOLUME /export/  

