FROM adite/base  
MAINTAINER tescom <tescom@atdt01410.com>  
  
ENV SERVER_IP 127.0.0.1  
ENV SERVER_NAME db  
  
# Install packages  
WORKDIR /tmp  
RUN apt-get update && \  
apt-get install -y libfontconfig wget adduser bc && \  
wget https://grafanarel.s3.amazonaws.com/builds/grafana_2.6.0_amd64.deb && \  
dpkg -i grafana_2.6.0_amd64.deb && \  
git clone https://github.com/t2sc0m/grafana-dashboards.git && \  
cp -r grafana-dashboards/dashboards /var/lib/grafana && \  
chown grafana:grafana /var/lib/grafana -R && \  
wget
https://github.com/prometheus/prometheus/releases/download/0.17.0rc2/prometheus-0.17.0rc2.linux-
amd64.tar.gz && \  
mkdir -p /usr/local/prometheus && \  
tar zxf prometheus-0.17.0rc2.linux-amd64.tar.gz -C /usr/local/prometheus
--strip-components=1 && \  
sed -i 's/step_input:""/step_input:c.target.step/; s/ HH:MM/ HH:mm/;
s/,function(c)/,"templateSrv",function(c,g)/;
s/expr:c.target.expr/expr:g.replace(c.target.expr,c.panel.scopedVars)/'
/usr/share/grafana/public/app/plugins/datasource/prometheus/query_ctrl.js && \  
sed -i 's/h=a.interval/h=g.replace(a.interval, c.scopedVars)/'
/usr/share/grafana/public/app/plugins/datasource/prometheus/datasource.js && \  
rm -rf /tmp/* && \  
apt-get clean  
  
# Make prometheus config file  
ADD make_config.sh /make_config.sh  
RUN touch /usr/local/prometheus/prometheus.yml  
  
# Add grafana config file  
ADD grafana.ini /etc/grafana/grafana.ini  
  
ADD startup.sh /startup.sh  
RUN chmod 0755 /startup.sh  
  
EXPOSE 3000  
EXPOSE 9090  
VOLUME /usr/local/prometheus/data  
  
WORKDIR /usr/local/prometheus  
CMD ["/startup.sh"]  

