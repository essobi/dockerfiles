FROM linuxserver/baseimage.apache  
MAINTAINER furiousgeorge <furiousgeorgecode@gmail.com>  
  
# copy sources.list  
COPY sources.list /etc/apt/  
  
ENV APTLIST="libapache2-mod-php5 wget inotify-tools php5-gd php5-sqlite
php5-mcrypt php5-tidy php5-mysql libapache2-mod-proxy-html fail2ban iptables
exim4 bsd-mailx whois"  
# install main packages  
RUN apt-get update -q && \  
apt-get install $APTLIST -qy && \  
  
# cleanup  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add some files  
ADD services/ /etc/service/  
ADD jail.local /tmp/jail.local  
RUN chmod 666 /tmp/jail.local && chown abc:abc /tmp/jail.local  
RUN chmod -v +x /etc/service/*/run /etc/service/*/finish /etc/my_init.d/*.sh  
RUN mkdir -p /config/fail2ban/log  
  
# Update apache configuration with this one  
RUN a2enmod proxy proxy_http proxy_ajp rewrite deflate substitute headers
proxy_balancer proxy_connect proxy_html xml2enc authnz_ldap  
  
# So fail2ban doesn't fail  
RUN touch /var/log/auth.log  
  
# ports and volumes  
EXPOSE 80 443  
VOLUME /config  

