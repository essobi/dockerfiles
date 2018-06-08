FROM scratch  
  
ADD base.tar.xz /  
  
ENV PS1 "\u@\h:\w# "  
RUN touch /var/log/lastlog  
  
EXPOSE 22/tcp  
  
CMD ["/usr/sbin/dropbear", "-RFE", "-p", "22"]  

