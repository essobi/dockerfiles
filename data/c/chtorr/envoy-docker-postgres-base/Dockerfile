FROM envoyproxy/envoy:v1.6.0 AS envoy  
  
FROM postgres:9.6.8  
COPY \--from=envoy /usr/local/bin/envoy /usr/local/bin/envoy  
  
ENV TINI_VERSION v0.18.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
COPY envoy.yaml /etc/  
  
COPY start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start.sh  
  
ENTRYPOINT ["/tini", "-g", "--"]  
CMD ["start.sh"]

