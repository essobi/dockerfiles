FROM frolvlad/alpine-glibc:alpine-3.3_glibc-2.23  
ENV FACTORIO_VER 0.12.29  
RUN \  
apk add --no-cache \  
curl \  
tar \  
&& mkdir -p /opt/factorio \  
&& curl -o factorio.tar.gz -SLk https://www.factorio.com/get-
download/${FACTORIO_VER}/headless/linux64 \  
&& tar --strip-components=1 -xzf factorio.tar.gz -C /opt/factorio \  
&& rm factorio.tar.gz  
  
COPY ./docker-entrypoint.sh /  
  
RUN chmod +x /docker-entrypoint.sh  
  
VOLUME ["/opt/factorio/saves", "/opt/factorio/mods"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 34197/udp  
  
CMD ["--start-server", "save"]

