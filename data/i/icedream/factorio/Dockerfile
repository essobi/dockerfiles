FROM debian:jessie-slim  
  
ARG FACTORIO_VERSION=0.14.23  
ARG FACTORIO_HEADLESS_URL=https://www.factorio.com/get-
download/${FACTORIO_VERSION}/headless/linux64  
ARG
FACTORIO_HEADLESS_SHA512=527d83b33e39fefcdc15a12febdc72bb3e6bae755f4adbc5721eae1408137dea9b8a5f56a0095b60c0bafd67b4eacf0f993e40097c369f291ab241943a90a4e9  
  
# Unpack and reconfigure Factorio  
ADD ${FACTORIO_HEADLESS_URL} /var/tmp/factorio.tar.gz  
RUN \  
echo "${FACTORIO_HEADLESS_SHA512} /var/tmp/factorio.tar.gz" |\  
sha512sum -c --strict - &&\  
\  
mkdir -p /opt &&\  
tar vxf /var/tmp/*.tar* -C /opt/ &&\  
rm -rf /var/tmp/* /tmp/* &&\  
\  
for f in /opt/factorio/bin/x64/*; do \  
chmod -v +x "$f"; \  
done  
  
# Reconfigure Factorio  
COPY config-path.cfg /opt/factorio/config-path.cfg  
COPY config /config/  
  
# Create an empty write data folder  
WORKDIR /data  
  
VOLUME ["/config", "/data"]  
  
EXPOSE 34197/udp  
  
CMD ["/opt/factorio/bin/x64/factorio", "--start-server-load-latest", "--mod-
directory", "./mods"]  

