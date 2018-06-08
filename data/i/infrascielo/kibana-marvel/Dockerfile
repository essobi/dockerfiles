FROM kibana  
ENV PATH /opt/kibana/bin:$PATH  
  
RUN kibana plugin --install elasticsearch/marvel/latest \  
&& chown -R kibana:kibana /opt/kibana  
  

