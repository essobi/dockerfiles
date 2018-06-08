FROM kibana:5.2.0  
LABEL Description="kibana"  
  
ENV KIBANA_PWD="changeme" \  
CA_PATH='/usr/share/elasticsearch/config/searchguard/ssl/ca/root-ca.pem'  
RUN /usr/share/kibana/bin/kibana-plugin install
https://github.com/floragunncom/search-guard-kibana-
plugin/releases/download/v5.2.0-1/searchguard-kibana-5.2.0-1.zip  
COPY kibana.yml /etc/kibana/kibana.yml  
COPY entrypoint.sh /  
  
COPY kibana.yml /.backup/kibana/kibana.yml  
  
VOLUME /etc/kibana  
EXPOSE 5601  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["kibana"]  
  

