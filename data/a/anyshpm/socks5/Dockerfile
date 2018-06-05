# ss5  
FROM centos:7  
MAINTAINER Anyshpm Chen <anyshpm@anyshpm.com>  
  
RUN groupadd -r ss5 && useradd -r -g ss5 ss5  
  
ENV SS5_VERSION 3.8.9-8  
COPY ss5-3.8.9-8.x86_64.rpm /tmp  
COPY entrypoint.sh /usr/local/bin/  
  
RUN rpm -ivh /tmp/ss5-3.8.9-8.x86_64.rpm && \  
sed -i "/#auth/a\auth 0.0.0.0\/0 - -" /etc/opt/ss5/ss5.conf && \  
sed -i "/#permit/a\permit - 0.0.0.0\/0 - 0.0.0.0\/0 - - - - - "
/etc/opt/ss5/ss5.conf && \  
rm -f /tmp/ss5-3.8.9-8.x86_64.rpm && \  
chmod +x /usr/local/bin/entrypoint.sh && \  
mkdir -p /var/log/ss5 && \  
touch /var/log/ss5/ss5.log  
  
ENTRYPOINT ["entrypoint.sh"]  
  
EXPOSE 1080/tcp  
  
CMD ["tail", "-f", "/var/log/ss5/ss5.log"]  

