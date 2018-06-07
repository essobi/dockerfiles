FROM alpine:3.4  
RUN mkdir /telegram && \  
adduser -D telegram  
  
COPY . /telegram/  
  
# This could be even smaller if we disable Python (there's a bug preventing
the configure flag from working currently)  
RUN apk --no-cache add readline readline-dev libconfig libconfig-dev openssl
openssl-dev build-base libevent libevent-dev python-dev jansson jansson-dev &&
\  
cd /telegram && \  
./configure --enable-json --disable-liblua --disable-readline && \  
make && \  
apk del readline-dev libconfig-dev openssl-dev build-base libevent-dev python-
dev jansson-dev  
  
RUN apk --no-cache add curl && \  
curl -L "https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64" -o /bin/dumb-init && \  
chmod +x /bin/dumb-init && \  
apk del ca-certificates curl  
  
WORKDIR /telegram  
  
USER telegram  
  
EXPOSE 4458  
ENTRYPOINT ["/bin/dumb-init", "--"]  
  
CMD ["bin/telegram-cli", "-k", "tg-server.pub", "--json", "-P", "4458", "--
accept-any-tcp", "--disable-readline"]  

