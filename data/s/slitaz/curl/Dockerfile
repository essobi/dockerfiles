FROM scratch  
  
ADD slitaz-curl.tar.xz /  
  
ENV PS1 "\u@\h:\w# "  
EXPOSE 80  
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

