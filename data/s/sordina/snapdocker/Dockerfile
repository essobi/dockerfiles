  
# For some reason the resolver ends up being 4.2 anyway...  
FROM haskell:7.10.3  
# Lock stack to 5.4 for this build  
#  
RUN mkdir /etc/stack  
RUN stack update  
RUN stack --resolver=lts-5.4 install microlens  
RUN echo "resolver: lts-5.4" >> /root/.stack/global-project/stack.yaml  
  
# Big packages  
#  
RUN stack install snap  
RUN stack install errors  
RUN stack install bytestring  
RUN stack install aeson  
RUN stack install base  
RUN stack install containers  
RUN stack install lens  
RUN stack install lens-aeson  
RUN stack install mtl  
RUN stack install text  
RUN stack install transformers  
RUN stack install unordered-containers  
RUN stack install wreq  
  
CMD echo DONE  

