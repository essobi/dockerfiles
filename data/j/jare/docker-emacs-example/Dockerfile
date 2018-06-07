FROM jare/emacs:latest  
  
MAINTAINER JAremko <w3techplaygound@gmail.com>  
  
ENV UNAME="jare"  
RUN apt-get update && apt-get install firefox \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p ${UHOME}  
  
COPY .emacs.d ${UHOME}/.emacs.d  
  
# Create ${UNAME} user and install Emacs packages  
RUN asEnvUser emacs -nw -batch -u ${UNAME} -q -kill  

