FROM alpine  
  
RUN apk update \  
&& apk add wget \  
&& cd /tmp \  
&& wget https://www.multichain.com/download/multichain-1.0.4.tar.gz -nv --no-
check-certificate \  
&& tar -xvzf multichain-1.0.4.tar.gz \  
&& cd multichain-1.0.4 \  
&& mv multichaind multichain-* /usr/local/bin \  
&& rm -rf /tmp/multichain* \  
&& rm -rf /var/cache/apk/*  
  
CMD ["/bin/bash"]  

