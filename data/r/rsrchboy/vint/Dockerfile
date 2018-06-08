# Tiny little vint image that will lint whatever's passed in on STDIN  
#  
# Chris Weyl <cweyl@alumni.drew.edu> 2017  
FROM python:2.7-alpine  
MAINTAINER Chris Weyl <cweyl@alumni.drew.edu>  
  
RUN pip --no-cache-dir install vim-vint  
# COPY do-vint.sh /bin/do-vint.sh  
ENTRYPOINT [ "vint" ]  

