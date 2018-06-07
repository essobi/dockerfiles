FROM cimpress/git2consul:0.12.13  
MAINTAINER Doug Clow @ MomentFeed  
  
# Needed for ssh-keyscan  
RUN apk update \  
&& apk add openssh-client  
  
# Install Consul  
ADD https://releases.hashicorp.com/consul/1.0.7/consul_1.0.7_linux_amd64.zip
/tmp/  
RUN unzip -d /usr/bin /tmp/consul_1.0.7_linux_amd64.zip && \  
rm /tmp/consul_1.0.7_linux_amd64.zip  
  
RUN adduser -h /home/git2consul -D git2consul \  
&& mkdir /home/git2consul/.ssh \  
&& chown git2consul /home/git2consul/.ssh \  
&& mkdir /var/lib/git2consul_cache \  
&& chown git2consul /var/lib/git2consul_cache \  
&& chown git2consul /etc/git2consul.d  
  
COPY docker-entrypoint.sh /  
RUN chmod 755 /docker-entrypoint.sh  
  
USER git2consul  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
CMD [ "/usr/bin/node", \  
"/usr/lib/node_modules/git2consul" \  
]  

