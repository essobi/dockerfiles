FROM beginor/ubuntu-china:16.04  
LABEL maintainer="beginor <beginor@qq.com>"  
  
ENV GEOSERVER_HOME=/geoserver  
  
COPY src/docker-entrypoint.sh /usr/bin/  
COPY ["src/web.xml", "src/install.sh", "/tmp/"]  
  
RUN /tmp/install.sh  
  
EXPOSE 8080  
VOLUME ["/geoserver/data_dir","/geoserver/logs"]  
  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  
  
HEALTHCHECK \--interval=30s --timeout=30s --start-period=30s --retries=3 \  
CMD curl
"http://127.0.0.1:8080/geoserver/ows?service=wfs&version=2.0.0&request=GetCapabilities"
|| exit 1  

