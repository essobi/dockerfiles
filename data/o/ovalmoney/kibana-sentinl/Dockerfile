FROM docker.elastic.co/kibana/kibana:5.5.2  
ENV SENTINL_VERSION 5.5.2  
RUN kibana-plugin remove x-pack && \  
kibana-plugin install
https://github.com/sirensolutions/sentinl/releases/download/tag-${SENTINL_VERSION%.*}/sentinl-v${SENTINL_VERSION}.zip  
  
COPY config/kibana.yml /usr/share/kibana/config/  
  
CMD ["/usr/local/bin/kibana-docker"]

