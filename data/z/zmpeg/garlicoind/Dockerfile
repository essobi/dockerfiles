FROM alpine  
  
RUN apk --update add git  
RUN apk --update add openssh  
RUN apk --update add libevent-dev  
RUN apk --update add boost-dev  
RUN apk --update add autoconf  
RUN apk --update add automake  
RUN apk --update add libtool  
RUN apk --update add g++  
RUN apk --update add openssl-dev  
RUN apk --update add make  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm /var/cache/apk/*  
  
WORKDIR /root/Garlicoin  
RUN git clone \--depth 1 https://github.com/GarlicoinOrg/Garlicoin.git .  
COPY install-berkeleydb-4.8.sh /root/Garlicoin/  
RUN ./install-berkeleydb-4.8.sh  
RUN ./autogen.sh  
RUN ./configure --without-gui LDFLAGS="-L/root/Garlicoin/db4/lib/"
CPPFLAGS="-I/root/Garlicoin/db4/include/"  
RUN make  
  
FROM alpine  
RUN apk --update add libevent  
RUN apk --update add boost-dev  
RUN apk --update add openssl  
RUN mkdir -p /root/bin  
ENV PATH="/root/bin:$PATH"  
COPY \--from=0 /root/Garlicoin/src/garlicoind /root/bin  
COPY \--from=0 /root/Garlicoin/src/garlicoin-cli /root/bin  
COPY \--from=0 /root/Garlicoin/src/garlicoin-tx /root/bin  
COPY entrypoint.sh /root/bin  
ENTRYPOINT ["entrypoint.sh"]

