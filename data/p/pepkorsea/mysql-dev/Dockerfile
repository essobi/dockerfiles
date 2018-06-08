# MySQL container for local development  
FROM mysql:5.7  
MAINTAINER Max Milton <max.milton@pepkor.com.au>  
  
# Allow external access  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# Harden image by unsetting SUID on all executables  
RUN for i in `find / -perm +6000 -type f`; do chmod a-s $i; done  

