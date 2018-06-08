FROM alpine:3.2  
ENV NOMAD_VERSION 0.3.1  
ENV NOMAD_SHA256
467fcebe9f0a349063a4f16c97cb71d9c57451fc1f10cdb2292761cf56542671  
ENV GLIBC_VERSION "2.23-r1"  
RUN apk --update add curl ca-certificates && \  
curl -Ls https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk >
/tmp/glibc-${GLIBC_VERSION}.apk && \  
apk add --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk && \  
rm -rf /tmp/glibc-${GLIBC_VERSION}.apk /var/cache/apk/*  
ADD
https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip
/tmp/nomad.zip  
RUN echo "${NOMAD_SHA256} /tmp/nomad.zip" > /tmp/nomad.sha256 \  
&& sha256sum -c /tmp/nomad.sha256 \  
&& cd /bin \  
&& unzip /tmp/nomad.zip \  
&& chmod +x /bin/nomad \  
&& rm /tmp/nomad.zip  
  
EXPOSE 4646  
EXPOSE 4647  
EXPOSE 4648  
EXPOSE 4648/udp  
  
ENTRYPOINT ["/bin/nomad"]  
  

