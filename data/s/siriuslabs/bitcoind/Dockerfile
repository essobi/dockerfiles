FROM siriuslabs/alpine  
  
# add community and testing repo  
RUN echo "@community http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
# install the packges we need  
RUN apk add --no-cache bash \  
shadow \  
bitcoin@testing \  
bitcoin-cli@testing  
  
ENV BITCOIN_HOME /home/bitcoin  
  
ENV BITCOIN_DATA /home/bitcoin/.bitcoin  
  
RUN usermod -m -d "$BITCOIN_HOME" bitcoin \  
&& mkdir -p "$BITCOIN_DATA" \  
&& chown -R bitcoin:bitcoin "$BITCOIN_HOME" \  
&& rm -rf /etc/bitcoin.conf  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 8332 8333 18332 18333  
VOLUME ["/home/bitcoin/.bitcoin"]  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
CMD ["bitcoind"]  

