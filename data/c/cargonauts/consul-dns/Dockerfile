FROM cargonauts/consul:0.5.0  
ADD consul-dns.json /opt/config/consul-dns.json  
ENTRYPOINT /consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul
-config-dir /opt/config/ -client 0.0.0.0  

