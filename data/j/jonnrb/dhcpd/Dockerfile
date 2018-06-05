from alpine:latest  
  
run apk update \  
&& apk add dhcp wget ca-certificates  
  
# Get docker-gen  
env DOCKER_GEN_VERSION 0.7.3  
run wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
run touch /var/lib/dhcp/dhcpd.leases  
  
add dhcpd.conf.tmpl /etc/dhcp/dhcpd.conf.tmpl  
  
add init.sh /  
cmd ["/init.sh"]  
  

