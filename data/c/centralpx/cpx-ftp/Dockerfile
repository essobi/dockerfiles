FROM stilliard/pure-ftpd  
  
MAINTAINER Galen Parker <galen.parker@gmail.com>  
  
VOLUME /home/ftpuser /etc/pure-ftpd  
  
CMD /usr/sbin/pure-ftpd -c 30 -C 5 -l puredb:/etc/pure-ftpd/pureftpd.pdb -E -j
-R -p 30000:30009 -P $PUBLICHOST  

