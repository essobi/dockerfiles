FROM debian:jessie-slim  
  
RUN apt-get update && apt-get install -y \  
build-essential cmake curl \  
&& cd /tmp \  
&& curl -L https://github.com/fluent/fluent-bit/archive/v0.11.2.tar.gz \  
| tar -xz --strip 1 \  
&& cmake -DFLB_DEBUG=On -DFLB_TRACE=On -DFLB_JEMALLOC=On -DFLB_BUFFERING=On .
\  
&& make \  
&& make install \  
&& rm -rf /tmp/* \  
&& apt-get remove \--purge --auto-remove -y \  
build-essential cmake make curl  
  
COPY ./conf /etc/fluent  
  
# USER nobody:nobody  
CMD ["fluent-bit", "--config=/etc/fluent/fluent-bit.conf"]  

