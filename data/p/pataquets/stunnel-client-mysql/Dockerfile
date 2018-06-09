FROM pataquets/stunnel:xenial  
  
ADD client-mysql /etc/stunnel/confs-available/  
RUN \  
ln -vs \  
/etc/stunnel/confs-available/client-mysql \  
/etc/stunnel/conf.d/ \  
&& \  
nl /etc/stunnel/conf.d/client-mysql && \  
rm -v /etc/stunnel/conf.d/10-global-verify-peer  

