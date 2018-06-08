FROM nginx:1.7.9  
ENV KIBANA_VERSION 3.1.2  
ADD
https://download.elasticsearch.org/kibana/kibana/kibana-$KIBANA_VERSION.tar.gz
/tmp/kibana.tar.gz  
RUN tar zxf /tmp/kibana.tar.gz && \  
mv kibana-$KIBANA_VERSION /opt/kibana && \  
rm /tmp/kibana.tar.gz  
  
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.org  
ADD run.sh /usr/local/bin/run  
  
EXPOSE 80  
CMD ["/usr/local/bin/run"]  

