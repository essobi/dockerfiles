FROM wow73611/ubuntu  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
RUN \  
sed -i 's/^# \\(.*-backports\s\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y haproxy && \  
sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy && \  
rm -rf /var/lib/apt/lists/*  
  
ADD haproxy.cfg /etc/haproxy/haproxy.cfg  
  
EXPOSE 80  
CMD ["haproxy","-f","/etc/haproxy/haproxy.cfg"]  

