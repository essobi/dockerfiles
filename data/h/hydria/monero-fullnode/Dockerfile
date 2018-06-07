FROM debian:stretch  
LABEL MAINTAINER Hydria  
  
ENV RELEASE="0.11.1.0"  
ENV
CHECKSUM="6581506f8a030d8d50b38744ba7144f2765c9028d18d990beb316e13655ab248"  
ENV PACKAGES="\  
bzip2 \  
curl"  
RUN apt-get update && apt-get install $PACKAGES -y  
WORKDIR /root  
RUN curl https://downloads.getmonero.org/cli/monero-
linux-x64-v$RELEASE.tar.bz2 -O &&\  
echo '6581506f8a030d8d50b38744ba7144f2765c9028d18d990beb316e13655ab248 monero-
linux-x64-v0.11.1.0.tar.bz2' | sha256sum -c - &&\  
tar -xjvf monero-linux-x64-v$RELEASE.tar.bz2 &&\  
rm monero-linux-x64-v$RELEASE.tar.bz2 &&\  
cp ./monero-v$RELEASE/monerod . &&\  
rm -r monero-*  
  
VOLUME /root/.bitmonero  
EXPOSE 18080 18081  
ENTRYPOINT ["./monerod"]  
CMD ["--restricted-rpc", "--rpc-bind-ip=0.0.0.0", "--confirm-external-bind"]  

