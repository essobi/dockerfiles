FROM nginx:1.10.2-alpine  
RUN apk add --no-cache curl && apk add --no-cache unzip && curl -sSL
https://releases.hashicorp.com/consul-template/0.18.0/consul-
template_0.18.0_linux_amd64.zip > /tmp/consul-template.zip && \  
unzip /tmp/consul-template.zip -d /tmp && mv /tmp/consul-template
/usr/bin/consul-template && rm -f /tmp/consul-template.zip  
ENTRYPOINT ["/usr/bin/consul-template"]  
CMD
["-template","/etc/nginx/consul/nginx.tmpl:/etc/nginx/nginx.conf","-exec","nginx","-exec-
reload-signal","SIGHUP"]  

