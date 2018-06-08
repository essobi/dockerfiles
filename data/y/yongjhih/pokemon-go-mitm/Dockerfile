FROM node  
  
ENV POKEMON_GO_MITM_VERSION 2.0  
WORKDIR /src  
  
RUN apt-get update && \  
curl -L https://github.com/rastapasta/pokemon-go-
mitm/archive/v${POKEMON_GO_MITM_VERSION}.tar.gz -o - | gzip -d - | tar x && \  
mv pokemon-go-mitm-${POKEMON_GO_MITM_VERSION}/* /src/ && \  
rm -rf pokemon-go-mitm-${POKEMON_GO_MITM_VERSION} && \  
apt-get install -y libprotobuf-dev && \  
npm install && \  
npm install -g coffee-script && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["npm", "start"]  

