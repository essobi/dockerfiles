FROM pataquets/xinetd-mysql  
  
COPY \  
hosts.allow.oficina \  
hosts.allow.vmhosts \  
hosts.allow.google \  
/tmp/  
  
RUN \  
cat \  
/tmp/hosts.allow.oficina \  
/tmp/hosts.allow.vmhosts \  
/tmp/hosts.allow.google \  
| tee -a /etc/hosts.allow \  
&& \  
rm -v \  
/tmp/hosts.allow.oficina \  
/tmp/hosts.allow.vmhosts \  
/tmp/hosts.allow.google \  
&& \  
echo "ALL: ALL" | tee -a /etc/hosts.deny \  
&& \  
nl /etc/hosts.allow && \  
nl /etc/hosts.deny  

