FROM illallangi/ansible:latest as build  
ENV BITCOIN_VERSION=0.15.1  
ENV
BITCOIN_SHA256=387c2e12c67250892b0814f26a5a38f837ca8ab68c86af517f975a2a2710225b  
COPY build/* /etc/ansible.d/build/  
RUN /usr/local/bin/ansible-runner.sh build  
  
FROM illallangi/ansible:latest as image  
  
COPY \--from=build /usr/local/src/*.tar.gz /usr/local/src/  
COPY \--from=build /usr/local/src/bitcoin-0.15.1/bin/bitcoin-cli
/usr/local/bin/  
COPY \--from=build /usr/local/src/bitcoin-0.15.1/bin/bitcoin-qt
/usr/local/bin/  
COPY \--from=build /usr/local/src/bitcoin-0.15.1/bin/bitcoin-tx
/usr/local/bin/  
COPY \--from=build /usr/local/src/bitcoin-0.15.1/bin/bitcoind /usr/local/bin/  
COPY \--from=build /usr/local/src/bitcoin-0.15.1/bin/test_bitcoin
/usr/local/bin/  
  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
ENV UID=1024  
ENV USER=bitcoin  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/bitcoin-entrypoint.sh"]  

