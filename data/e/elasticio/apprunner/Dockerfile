FROM elasticio/cedarish:production  
  
# Install and configure Tini  
# https://github.com/krallin/tini  
ENV TINI_VERSION v0.17.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
ADD ./runner/ /runner  
#ADD ./bin/sdutil /bin/sdutil  
ENTRYPOINT ["/tini", "-v", "-e", "143", "--", "/runner/init"]  

