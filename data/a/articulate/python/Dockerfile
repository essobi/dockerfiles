FROM python:3.6-jessie  
  
ENV SERVICE_USER service  
RUN apt-get update -qq \  
&& apt-get -y install groff \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD https://raw.githubusercontent.com/articulate/docker-consul-template-
bootstrap/master/install.sh /tmp/consul_template_install.sh  
RUN bash /tmp/consul_template_install.sh && rm /tmp/consul_template_install.sh  
  
# UID and GID need to be hardcoded to 90001 to match the service user on the
host instance for volume mounting  
RUN groupadd -g 90001 $SERVICE_USER && useradd -u 90001 --create-home --home
/home/$SERVICE_USER \--gid $SERVICE_USER \--shell /bin/bash $SERVICE_USER  
  
ADD https://raw.githubusercontent.com/articulate/docker-consul-template-
bootstrap/master/wait-for-it.sh /wait-for-it.sh  
RUN chmod a+rx /wait-for-it.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

