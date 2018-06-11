FROM fedora:21  
MAINTAINER Tim Robinson <tim@voltgrid.com>  
  
RUN cp -a /usr/share/zoneinfo/UTC /etc/localtime; \  
echo -e "ZONE=\"UTC\"\nUTC=True" > /etc/sysconfig/clock  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["/usr/bin/s6-svscan","/etc/s6"]  
CMD []  
  
RUN \  
yum -q -y install nginx tar wget && \  
yum -q -y clean all  
  
RUN \  
wget --quiet -O - https://github.com/hashicorp/consul-
template/releases/download/v0.7.0/consul-template_0.7.0_linux_amd64.tar.gz |
tar -C /usr/local/bin --strip 1 -zxf - && \  
wget --quiet -O - https://github.com/just-containers/skaware-
builder/releases/download/v1.8.0/s6-2.1.3.0-linux-amd64-bin.tar.gz | tar -C /
-zxf - && \  
chown root:root /usr/local/bin/consul-template && \  
mkdir -p /consul-template/{config,templates,output} && \  
echo '#{{file "/etc/redhat-release"}}' > /consul-template/templates/test.ctmpl
&& \  
echo "daemon off;" >> /etc/nginx/nginx.conf  
  
COPY consul-template.conf /consul-template/config/00-consul.conf  
COPY test.conf /consul-template/config/01-test.conf  
COPY s6 /etc/s6/  
COPY nginx-reload /usr/local/bin/nginx-reload  

