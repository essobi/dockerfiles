FROM tazounet/cerebro  
  
RUN wget -O /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd \  
&& mkdir -p /etc/confd/{conf.d,templates}  
  
COPY files/application.toml /etc/confd/conf.d/application.toml  
COPY files/application.conf.tmpl /etc/confd/templates/application.conf.tmpl  
  
CMD ["confd", "-onetime", "-backend", "env"]  

