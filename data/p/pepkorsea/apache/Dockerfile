FROM httpd:2.4  
MAINTAINER Max Milton <max.milton@pepkor.com.au>  
  
# Harden image by unsetting SUID on all executables  
RUN for i in `find / -perm +6000 -type f`; do chmod a-s $i; done  

