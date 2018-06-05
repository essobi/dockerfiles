FROM articulate/consul-agent:0.7  
ADD ./config /config/  
ADD ./entrypoint.sh /bin/entrypoint.sh  
RUN chmod +x /bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh", "/bin/consul", "agent", "-server", "-config-
dir=/config"]  

