FROM mongo:3.2.0  
ENV CACHE_DIR="/etc/docker-mongodb" \  
MAIN_USER="mongodb"  
ENV BUILD_DIR="${CACHE_DIR}/build" \  
RUNTIME_DIR="${CACHE_DIR}/runtime"  
#COPY assets/build ${BUILD_DIR}  
#RUN bash ${BUILD_DIR}/install.sh  
COPY entrypoint.sh /extended-entrypoint.sh  
RUN chmod 755 /extended-entrypoint.sh  
ENTRYPOINT ["/extended-entrypoint.sh"]  
CMD ["app:start"]  
  
COPY assets/runtime ${RUNTIME_DIR}  

