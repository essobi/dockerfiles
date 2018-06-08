FROM scratch  
  
ADD base.tar.xz /  
  
ENV PS1 "\u@\h:\w# "  
EXPOSE 22/tcp  
  
CMD ["/usr/sbin/dropbear", "-RFEs", "-p", "22"]  

