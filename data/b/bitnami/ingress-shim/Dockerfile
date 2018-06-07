FROM bitnami/minideb:jessie as buildenv  
  
RUN install_packages ca-certificates wget  
RUN wget -nc -P /tmp/bitnami/pkg/cache/
https://downloads.bitnami.com/files/stacksmith/ingress-
shim-0.2.5-0-linux-x64-debian-8.tar.gz && \  
echo "03dbcf05da7267d4bb804a981b67b254fed28d011eb58464f37a55f6d784378f
/tmp/bitnami/pkg/cache/ingress-shim-0.2.5-0-linux-x64-debian-8.tar.gz" |
sha256sum -c - && \  
tar -zxf /tmp/bitnami/pkg/cache/ingress-shim-0.2.5-0-linux-x64-debian-8.tar.gz
-P --transform 's|^[^/]*/files|/opt/bitnami|' \--wildcards '*/files' && \  
rm -rf /tmp/bitnami/pkg/cache/ingress-shim-0.2.5-0-linux-x64-debian-8.tar.gz  
  
##################  
FROM bitnami/minideb:jessie  
LABEL maintainer "Bitnami <containers@bitnami.com>"  
  
COPY \--from=buildenv /opt/bitnami/ingress-shim /opt/bitnami/ingress-shim  
ENV BITNAMI_APP_NAME="ingress-shim" \  
BITNAMI_IMAGE_VERSION="0.2.5-r13" \  
PATH="/opt/bitnami/ingress-shim/bin:$PATH"  
RUN install_packages ca-certificates  
  
WORKDIR /opt/bitnami/ingress-shim  
USER 1001  
ENTRYPOINT ["/opt/bitnami/ingress-shim/bin/ingress-shim"]  

