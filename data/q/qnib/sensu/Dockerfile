### Add Sensu to the mix  
FROM qnib/syslog  
  
ADD etc/yum.repos.d/sensu.repo /etc/yum.repos.d/  
RUN dnf install -y sensu nmap && \  
mkdir -p /var/run/sensu && \  
chown sensu: /var/run/sensu && \  
mkdir -p /etc/sensu/init.d/ \  
&& /opt/sensu/embedded/bin/gem install sensu-plugins-influxdb  
  
ENV SENSU_CLIENT=false \  
SENSU_API=false \  
SENSU_SERVER=false \  
SENSU_FORCE_CLIENT=false \  
SENSU_RABBITMQ_HOST=rabbitmq.service.consul \  
SENSU_RABBITMQ_VHOST=sensu \  
SENSU_RABBITMQ_USER=sensu \  
SENSU_RABBITMQ_PASSWD=pass  
ADD etc/sensu/settings.json /etc/sensu/  
ADD etc/supervisord.d/*.ini /etc/supervisord.d/  
ADD etc/consul.d/*.json /etc/consul.d/  
ADD /opt/qnib/sensu/server/bin/start.sh /opt/qnib/sensu/server/bin/  
ADD /opt/qnib/sensu/api/bin/start.sh /opt/qnib/sensu/api/bin/  
ADD /opt/qnib/sensu/client/bin/start.sh /opt/qnib/sensu/client/bin/  
ADD etc/consul-templates/sensu/*.json.ctmpl /etc/consul-templates/sensu/  
ADD etc/sensu/conf.d/slack/slack.json /etc/sensu/conf.d/slack/  
RUN /opt/sensu/embedded/bin/gem install sensu-plugins-slack  

