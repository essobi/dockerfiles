FROM docker:17.03  
RUN \  
apk add --no-cache bash  
  
ENV EMAIL=  
  
ENV CERTS_DIR=/etc/simp_le/  
ENV LISTEN_PORT=9002  
ENV SERVER_NAME=simp_le  
ENV DOCKER_SIMP_LE_ARGS=  
ENV DOCKER_RUN_SIMP_LE_ARGS=  
ENV AUTO_CONF_D=/etc/simp_le-auto.d  
ENV AUTO_UPDATED_DIR=/etc/simp_le-auto-updated  
  
COPY gen /etc/periodic/weekly/gen  
COPY start /bin/start  
  
ENTRYPOINT ["/bin/start"]  

