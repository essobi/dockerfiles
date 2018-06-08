FROM prozeta/mother-baseimage:latest  
MAINTAINER Radek Slavicinsky "radek@blufor.cz"  
ADD run.sh /etc/service/tftp/run  
EXPOSE 69  
VOLUME /var/lib/tftpboot  
CMD ["/sbin/my_init"]

