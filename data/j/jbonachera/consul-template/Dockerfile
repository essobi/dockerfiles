FROM fedora:latest  
MAINTAINER Julien BONACHERA <julien@bonachera.fr>  
  
ONBUILD COPY consul-template.d/* /etc/consul-template/  
ONBUILD COPY supervisord.conf /etc/supervisord.d/service.ini  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  
RUN dnf install -y supervisor && dnf clean all  
ENV VERSION=0.14.0  
RUN curl -sLo /opt/ct.zip https://releases.hashicorp.com/consul-
template/${VERSION}/consul-template_${VERSION}_linux_amd64.zip && \  
python3 -m zipfile -e /opt/ct.zip /usr/bin/ && \  
chmod +x /usr/bin/consul-template && \  
rm -rf /go /opt/ct.zip  
RUN mkdir /etc/consul-template/  
COPY consul-template.ini /etc/supervisord.d/consul-template.ini  
COPY rpcinterface.ini /etc/supervisord.d/rpcinterface.ini  
COPY consul-template.conf /etc/consul-template/base.conf  
COPY ct.sh /usr/local/bin/ct.sh  

