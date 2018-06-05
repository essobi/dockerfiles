FROM ethcore/parity  
  
RUN apt-get update  
RUN apt-get install -y expect  
  
RUN mkdir /app  
WORKDIR /app  
ADD . /app  
  
# RUN ls # change this line to regenerate a new account  
RUN ./account_new.sh  
  
# this is optional, just to check that the line above ran  
RUN /build/parity/target/release/parity account list  
  
RUN ./prepare_config  
  
# check config (inspect this to see that prepare_config ran successfully, the
ADDRESS placeholder should be replaced with your coinbase)  
RUN cat ./config/chain.json  
  
EXPOSE 8545  
EXPOSE 8080  
CMD COINBASE=$(./get_coinbase) && /build/parity/target/release/parity -l all
--password ./password --unlock $COINBASE \--author $COINBASE \--chain
./config/chain.json --rpcaddr 0.0.0.0  
# CMD /build/parity/target/release/parity --unlock
0000000000000000000000000000000000000000 --password ./config/password --chain
./config/chain.json --rpcaddr 0.0.0.0 ; # in an ideal world  

