FROM prozeta/mother-baseimage:latest  
MAINTAINER Radek Slavicinsky "radek@blufor.cz"  
ADD run.sh /etc/service/foreman/run  
EXPOSE 80 443 3443  
VOLUME /etc/puppet /var/lib/puppet/ssl /opt/nginx/ssl  
CMD [ "/sbin/my_init" ]  

