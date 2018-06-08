FROM glen/pld:20160825  
RUN \  
uname -r && \  
rpm -q rpm poldek glibc && \  
echo  
  
RUN poldek -u glibc && \  
poldek --clean-whole  
  
RUN ls -l /lib64  

