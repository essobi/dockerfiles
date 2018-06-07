# Kibana  
FROM digitalwonderland/base:latest  
  
ADD ./src /  
  
RUN chmod +x /usr/local/sbin/start.sh  
  
# Install packages  
RUN rpm --rebuilddb && yum install -y tar && yum clean all  
  
# Install Kibana  
RUN cd /tmp \  
&& curl -O
https://download.elastic.co/kibana/kibana/kibana-4.1.2-linux-x64.tar.gz \  
&& tar xzf kibana-*.tar.gz \  
&& rm kibana-*.tar.gz \  
&& mv kibana-* /opt/kibana  
  
RUN groupadd -r kibana \  
&& useradd -c "Kibana" -g kibana -M -r -s /sbin/nologin kibana  
  
EXPOSE 5601  
ENTRYPOINT ["/usr/local/sbin/start.sh"]  

