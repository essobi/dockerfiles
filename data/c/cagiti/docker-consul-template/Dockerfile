FROM centos:latest  
  
ENV CONSUL_TEMPLATE_VERSION "0.13.0"  
RUN yum -y update && \  
yum -y install wget unzip  
  
RUN wget -nv "https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" && \  
unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
mv consul-template /usr/local/bin && \  
rm -f consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
RUN yum -y remove wget unzip  
  
ADD template.ctmpl /tmp  
  
EXPOSE 8543  

