FROM longkey1/firebase  
  
# Install hugo  
ENV HUGO_VESION 0.29  
RUN cd /tmp  
RUN wget
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VESION}/hugo_${HUGO_VESION}_Linux-64bit.tar.gz  
RUN tar xzvf hugo_${HUGO_VESION}_Linux-64bit.tar.gz  
RUN mv hugo /usr/local/bin/hugo  

