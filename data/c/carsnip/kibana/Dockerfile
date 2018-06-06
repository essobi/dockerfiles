FROM nginx  
MAINTAINER Mark Smithson mark@digital-morphosis.com  
ENV REFRESHED_AT 2015-01-07  
RUN apt-get update && apt-get install -y curl  
  
# Install Kibana  
RUN cd /tmp \  
&& curl -O https://download.elasticsearch.org/kibana/kibana/kibana-
latest.tar.gz \  
&& tar xzf kibana-*.tar.gz \  
&& rm kibana-*.tar.gz \  
&& mv kibana-*/* /usr/share/nginx/html  
  
ADD nginx-start.sh /usr/local/bin/nginx-start.sh  
RUN chmod ugo+x /usr/local/bin/nginx-start.sh  
  
ENTRYPOINT ["/usr/local/bin/nginx-start.sh"]

