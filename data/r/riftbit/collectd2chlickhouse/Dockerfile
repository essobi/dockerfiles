# CLD2CH docker  
#  
# VERSION 0.1  
FROM alpine:latest  
MAINTAINER Riftbit ErgoZ <ergozru@riftbit.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION=v0.0.10  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="CollectD2Clickhouse" \  
org.label-schema.description="CollectD to Clickhouse Gateway Container" \  
org.label-schema.url="https://riftbit.com/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/riftbit/docker-cld2ch" \  
org.label-schema.vendor="Riftbit Studio" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Riftbit ErgoZ"  
  
# Prepare APK CDNs  
RUN DIR=$(mktemp -d) && cd ${DIR} && \  
apk update && apk upgrade && \  
apk add --update wget tar bzip2 gzip ca-certificates && \  
mkdir -p /opt/cld2ch && \  
wget https://github.com/riftbit/go-cld2ch/releases/download/${VERSION}/cld2ch-
linux-amd64_${VERSION}.tar.gz && \  
tar zxf cld2ch-linux-amd64_${VERSION}.tar.gz && \  
cp ./cld2ch /opt/cld2ch/cld2ch && \  
cd /opt/cld2ch && chmod +x ./cld2ch && \  
rm -rf ${DIR} && \  
apk del wget tar bzip2 gzip ca-certificates curl && \  
rm -rf /var/cache/apk/*  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 25826:25826/udp  
  
CMD ["start_cld2ch"]  

