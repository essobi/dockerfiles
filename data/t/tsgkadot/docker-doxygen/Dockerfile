FROM alpine:3.6  
LABEL MAINTAINER tsgkdt <tsgkadot@gmail.com> \  
DESC Doxygen and SVN, Git  
  
RUN apk --update add doxygen graphviz subversion git && \  
rm -rf /var/cache/apk/*  
  
CMD ["doxygen", "-v"]  

