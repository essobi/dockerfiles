FROM centos:centos7  
  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
ENV REFRESHED_AT 2016_06_02  
  
COPY files /  
RUN useradd -u 950 -U -s /bin/false -M -r -G users docker && \  
yum upgrade -y && yum install -y epel-release inotify-tools net-tools && \  
mkdir /tmp/sockets && \  
yum install -y python-pip && pip install --upgrade pip && \  
yum install -y openssl-devel python-devel libffi-devel gcc && \  
pip install requests[security] && \  
yum autoremove -y openssl-devel python-devel libffi-devel gcc || true && \  
pip install supervisor && \  
yum clean all && \  
chmod -R 0755 /init/* /hooks/* && \  
chmod 777 /var/log  
  
ENTRYPOINT ["/bin/sh", "-e", "/init/entrypoint"]  
CMD ["run"]  

