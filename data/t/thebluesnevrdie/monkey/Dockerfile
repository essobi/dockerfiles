FROM thebluesnevrdie/base  
LABEL maintainer "Cody Crawford <me@codycrawford.net>"  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN curl -L http://apt.monkey-project.com/monkey.key | apt-key add - && \  
echo "deb http://apt.monkey-project.com/debian jessie main" >
/etc/apt/sources.list.d/monkey.list && \  
apt-get update && apt-get -y upgrade && \  
apt-get -y install monkey && \  
rm -f /var/log/monkey/access.log && \  
ln -sf /dev/stdout /var/log/monkey/access.log && \  
find / -path /sys -prune -o -path /proc -prune -o -user www-data -exec chown
root:root {} \; && \  
sed -i 's/User www-data/User root/' /etc/monkey/monkey.conf && \  
apt-get -y autoremove && rm -f /var/cache/apt/archives/*.deb  
  
EXPOSE 80 443  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["/usr/sbin/monkey"]  

