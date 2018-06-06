FROM cargonauts/consul-dns  
ADD 0.5.0_web_ui.tar.gz /web-ui  
ENTRYPOINT ["/consul", "agent", "-server", "-bootstrap-expect", "1", "-data-
dir", "/tmp/consul", "-config-dir", "/opt/config/", "-ui-dir", "/web-ui/dist",
"-client", "0.0.0.0"]  

