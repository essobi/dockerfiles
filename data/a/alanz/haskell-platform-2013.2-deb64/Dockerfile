FROM alanz/haskell-ghc-7.6.3-64  
MAINTAINER alan.zimm@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
##### haskell platform 2013.2.0.0 #################  
RUN wget http://www.haskell.org/platform/download/2013.2.0.0/haskell-
platform-2013.2.0.0.tar.gz  
  
RUN tar xvfz haskell-platform-2013.2.0.0.tar.gz  
  
RUN cd haskell-platform-2013.2.0.0 && ./configure  
RUN cd haskell-platform-2013.2.0.0 && make  
RUN cd haskell-platform-2013.2.0.0 && make install  
  
# Clean up  
RUN rm -fr haskell-platform-2013.2.0.0.tar.gz haskell-platform-2013.2.0.0  
  
# Note: to debug the partial build do the following  
# docker run -i -t alanz/haskell-platform-2013.2.0.0-64 /bin/bash  

