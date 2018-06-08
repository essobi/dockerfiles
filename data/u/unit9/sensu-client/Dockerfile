FROM unit9/sensu-base:latest  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
  
COPY check-sensu-config.sh /etc/rc.local.d/99-check-sensu-config  
COPY sensu-client.run /etc/service/sensu-client/run  
  
COPY check-kube.rb /etc/sensu/plugins/  

