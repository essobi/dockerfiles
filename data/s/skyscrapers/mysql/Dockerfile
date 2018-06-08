FROM skyscrapers/puppet:3.4.3  
MAINTAINER skyscrapers "support@skyscrapers.eu"  
ADD ./site.pp /etc/puppet/manifests/site.pp  
COPY ./docker-entrypoint.sh /usr/local/bin/  
  
RUN \  
git clone https://github.com/skyscrapers/puppetlabs-stdlib.git
/etc/puppet/modules/stdlib && \  
git clone https://github.com/skyscrapers/puppetlabs-mysql.git
/etc/puppet/modules/mysql && \  
puppet apply /etc/puppet/manifests/site.pp --verbose --detailed-exitcodes || [
$? -eq 2 ] && \  
update-rc.d -f mysqld remove && \  
chmod 755 /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 3306  
VOLUME /var/lib/mysql  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["mysqld"]  

