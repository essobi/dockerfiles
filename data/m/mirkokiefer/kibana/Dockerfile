  
FROM mirkokiefer/nginx  
  
RUN curl https://download.elasticsearch.org/kibana/kibana/kibana-3.1.0.tar.gz
> kibana.tar.gz  
  
RUN tar xvzf kibana.tar.gz --strip-components=1 --no-same-owner -C /data/www  

