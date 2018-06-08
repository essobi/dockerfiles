FROM debian:stretch  
MAINTAINER Yuya.Nishida.  
  
RUN apt-get update && \  
apt-get install -y quickml && \  
sed -r -e 's/^( *)(be_daemon)/\1#\2/' /usr/sbin/quickml >
/usr/local/sbin/quickml-foreground && \  
chmod a+x /usr/local/sbin/quickml-foreground && \  
install -m 755 -o list -g list -d /var/run/quickml  
COPY quickmlrc /etc/quickml/  
COPY entrypoint.sh /usr/local/bin/  
  
EXPOSE 10025  
VOLUME ["/var/lib/quickml"]  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["/usr/local/sbin/quickml-foreground"]  

