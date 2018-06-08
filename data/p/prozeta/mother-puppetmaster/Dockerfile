FROM prozeta/mother-baseimage:latest  
MAINTAINER Radek Slavicinsky "radek@blufor.cz"  
ADD node.rb /etc/puppet/node.rb  
ADD run.sh /etc/service/puppetmaster/run  
EXPOSE 8140  
VOLUME /etc/puppet/environments /etc/puppet/modules /var/lib/puppet  
CMD [ "/sbin/my_init" ]

