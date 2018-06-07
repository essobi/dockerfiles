FROM consul:latest  
COPY ./config/ /consul/config/  
ENTRYPOINT ["/bin/consul", "agent", "-server","-config-dir=/consul/config"]  

