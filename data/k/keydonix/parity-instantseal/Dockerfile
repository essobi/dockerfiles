FROM parity/parity:v1.11.1  
WORKDIR /  
COPY dev-key.json /parity/keys/DevChain/dev-key.json  
COPY chain-spec.json /parity/chain-spec.json  
COPY config.toml /parity/config.toml  
RUN echo "" > /parity/password  
  
ENTRYPOINT [ "/parity/parity", "--config", "/parity/config.toml" ]  
  
# docker image build --tag keydonix/parity-instant-seal .  
# docker container run --rm -it -p 8000:8000 -p 8001:8001 -p 8545:8545 -p
8180:8180 --name parity-instant-seal keydonix/parity-instant-seal  

