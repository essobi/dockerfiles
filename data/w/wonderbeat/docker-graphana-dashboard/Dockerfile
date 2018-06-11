FROM tutum/nginx  
MAINTAINER Denis Golovachev <borov.htid@gmail.com>  
  
ENV GRAFANA_VERSION 1.9.1  
RUN apt-get update && \  
apt-get install -y wget && \  
wget http://grafanarel.s3.amazonaws.com/grafana-${GRAFANA_VERSION}.tar.gz -O
grafana.tar.gz && \  
tar zxf grafana.tar.gz && \  
rm grafana.tar.gz && \  
rm -rf app && \  
mv grafana-${GRAFANA_VERSION} app && \  
apt-get autoremove -y wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /conf/config.js /app/config.js  
RUN rm /etc/nginx/sites-enabled/default && ln -s /conf/default
/etc/nginx/sites-enabled/default  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
CMD ["/run.sh"]  

