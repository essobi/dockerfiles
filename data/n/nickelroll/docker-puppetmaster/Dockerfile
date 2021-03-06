FROM nickelroll/jessie-baseimage:latest  
MAINTAINER Logan Attwood <logan@jnickel.com>  
  
ENV HOME /root  
ENV LANG en_CA.UTF-8  
RUN locale-gen en_CA.UTF-8  
  
# Fixes Docker Automated Build problem  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
# Install tools  
RUN apt-get update -q 2 && DEBIAN_FRONTEND=noninteractive \  
apt-get install -y apt-transport-https ca-certificates > /dev/null  
  
# Install Phusion Passenger Repository for Passenger/NGINX  
ADD conf/apt/passenger.list /etc/apt/sources.list.d/  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7
\  
&& chmod 0600 /etc/apt/sources.list.d/passenger.list  
  
# Install puppet, puppetmaster, nginx, and passenger  
RUN apt-get update -q 2 && DEBIAN_FRONTEND=noninteractive \  
apt-get install --yes -q 2 puppetmaster puppet \  
nginx-extras passenger >/dev/null  
  
# Install the nginx configuration and sites  
ADD conf/nginx/nginx.conf /etc/nginx/nginx.conf  
RUN ln -s /etc/nginx/sites-available/puppetmaster /etc/nginx/sites-
enabled/puppetmaster \  
&& rm /etc/nginx/sites-enabled/default  
  
# Install the Puppet Master's rack server  
RUN mkdir -p /usr/share/puppet/rack/puppetmaster/tmp
/usr/share/puppet/rack/puppetmaster/public \  
&& chown puppet:puppet -R /usr/share/puppet/rack/puppetmaster  
  
# Backup the Puppet config files, we'll regenerate them on boot if they're not
present  
RUN mkdir -p /usr/lib/puppet/default \  
&& find /etc/puppet -maxdepth 1 -type f -iname "*.conf" -exec mv {}
/usr/lib/puppet/default \; \  
&& cp /usr/share/puppet/ext/rack/config.ru /usr/lib/puppet/default  
  
# Install boot scripts  
ADD scripts/10_generate_puppet_config.rb /etc/my_init.d/  
ADD scripts/11_generate_nginx_site.rb /etc/my_init.d/  
ADD scripts/12_generate_puppetmaster_keys.sh /etc/my_init.d/  
RUN chmod +x /etc/my_init.d/*  
  
# Install runit scripts  
ADD scripts/nginx-startup.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
# Expose Puppet Master port  
EXPOSE 8140  
# use baseimage's init system  
CMD ["/sbin/my_init"]  

