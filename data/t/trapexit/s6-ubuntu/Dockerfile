FROM ubuntu:16.04  
ENV S6_OVERLAY=v1.19.1.1  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY}/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
RUN rm /tmp/s6-overlay-amd64.tar.gz  
ENTRYPOINT ["/init"]  
CMD ["bash"]  

