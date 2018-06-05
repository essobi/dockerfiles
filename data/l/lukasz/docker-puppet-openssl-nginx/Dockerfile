# puppet + nginx + openssl derived from lukasz/docker-scala  
#  
# Version 0.1  
FROM lukasz/docker-scala  
MAINTAINER Åukasz Budnik lukasz.budnik@gmail.com  
  
ADD init.pp /root/init.pp  
WORKDIR /root  
  
RUN wget http://apt.puppetlabs.com/puppetlabs-release-precise.deb  
RUN dpkg -i puppetlabs-release-precise.deb  
RUN rm puppetlabs-release-precise.deb  
RUN apt-get update  
  
RUN apt-get install -y puppet-common=2.7.22-1puppetlabs1  
RUN apt-get install -y puppet=2.7.22-1puppetlabs1  
RUN puppet module install jfryman/nginx  
RUN puppet module install --ignore-dependencies camptocamp/openssl  
RUN FACTER_fqdn=dev FACTER_port=9000 FACTER_random=`< /dev/urandom tr -dc _A-
Z-a-z-0-9 | head -c100` puppet apply init.pp  
# there is a bug in puppet openssl module need to invoke it twice!  
RUN FACTER_fqdn=dev FACTER_port=9000 FACTER_random=`< /dev/urandom tr -dc _A-
Z-a-z-0-9 | head -c100` puppet apply init.pp  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
EXPOSE 443  
ENTRYPOINT ["/usr/sbin/nginx"]  

