FROM kibana  
MAINTAINER System Insights <http://systeminsights.com>  
RUN gosu kibana chmod o+w /opt/kibana/optimize/  
  
RUN gosu kibana kibana plugin -i kibana/timelion  
RUN gosu kibana kibana plugin -i elasticsearch/marvel/latest  
RUN gosu kibana sed -ri "s!^(\\#\s*)?(server\\.basePath:).*!\2 '/kibana'!"
/opt/kibana/config/kibana.yml  
RUN gosu kibana timeout --foreground --signal=9 120 kibana || true  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 5601  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["kibana"]  

