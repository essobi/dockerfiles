FROM python:2.7  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
libcurl4-nss-dev \  
libapr1-dev \  
libsvn-dev  
  
RUN cd /usr/lib/x86_64-linux-gnu && \  
ln -s libsvn_subr-1.so.1 libsvn_subr-1.so.0 && \  
ln -s libsvn_delta-1.so.1 libsvn_delta-1.so.0 && \  
ln -s /usr/lib/x86_64-linux-gnu/libsasl2.so.2 /usr/lib/x86_64-linux-
gnu/libsasl2.so.3  
  
RUN rm /var/run && mv /run /var/run && ln -s /var/run /run  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

