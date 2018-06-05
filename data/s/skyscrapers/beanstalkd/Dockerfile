FROM skyscrapers/puppet:3.4.3  
MAINTAINER skyscrapers "support@skyscrapers.eu"  
ADD ./puppet/site.pp /etc/puppet/manifests/site.pp  
  
RUN \  
git clone https://github.com/skyscrapers/puppet-beanstalkd.git
/etc/puppet/modules/beanstalkd && \  
puppet apply /etc/puppet/manifests/site.pp --verbose --detailed-exitcodes || [
$? -eq 2 ] && \  
update-rc.d -f beanstalkd remove  
  
EXPOSE 11300  
CMD ["beanstalkd", "-p", "11300"]  

