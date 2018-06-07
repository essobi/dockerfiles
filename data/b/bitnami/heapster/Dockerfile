FROM bitnami/minideb:jessie as buildenv  
  
RUN install_packages ca-certificates wget  
RUN wget -nc -P /tmp/bitnami/pkg/cache/
https://downloads.bitnami.com/files/stacksmith/heapster-1.5.3-0-linux-x64-debian-8.tar.gz
&& \  
echo "784e2a9fe1c12fe680835448233e9ef1c2aacbd9d5721dbb9693b3adbf798aa6
/tmp/bitnami/pkg/cache/heapster-1.5.3-0-linux-x64-debian-8.tar.gz" | sha256sum
-c - && \  
tar -zxf /tmp/bitnami/pkg/cache/heapster-1.5.3-0-linux-x64-debian-8.tar.gz -P
--transform 's|^[^/]*/files|/opt/bitnami|' \--wildcards '*/files' && \  
rm -rf /tmp/bitnami/pkg/cache/heapster-1.5.3-0-linux-x64-debian-8.tar.gz  
  
##################  
FROM bitnami/minideb:jessie  
LABEL maintainer "Bitnami <containers@bitnami.com>"  
  
COPY \--from=buildenv /opt/bitnami/heapster /opt/bitnami/heapster  
ENV BITNAMI_APP_NAME="heapster" \  
BITNAMI_IMAGE_VERSION="1.5.3-r13" \  
PATH="/opt/bitnami/heapster/bin:$PATH"  
RUN install_packages ca-certificates  
  
EXPOSE 8082  
WORKDIR /opt/bitnami/heapster  
USER 1001  
ENTRYPOINT ["/opt/bitnami/heapster/bin/heapster"]  

