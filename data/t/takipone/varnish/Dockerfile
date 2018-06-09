#  
# Varnish Dockerfile  
#  
# https://github.com/otaki-ryuta/docker-varnish  
#  
# based on 14.04(Trusty Tahr)  
FROM dockerfile/ubuntu  
  
# Install Varnish.  
RUN \  
apt-get update && \  
apt-get install -y apt-transport-https && \  
curl https://repo.varnish-cache.org/ubuntu/GPG-key.txt | apt-key add - && \  
echo "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list && \  
apt-get update && \  
apt-get install -y varnish && \  
rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories.  
VOLUME ["/etc/varnish"]  
  
# Define working directory.  
WORKDIR /etc/varnish  
  
# Expose ports.  
EXPOSE 80  
# Define default command.  
CMD /usr/sbin/varnishd -F -f /etc/varnish/default.vcl -a :80 -s malloc,128m  

