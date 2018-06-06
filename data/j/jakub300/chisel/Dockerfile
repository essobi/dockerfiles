FROM node:8-stretch as pack  
  
COPY . /generator-chisel  
WORKDIR /generator-chisel  
RUN apt-get update && \  
apt-get install -y php-cli && \  
rm -rf /var/lib/apt/lists/* && \  
npm pack --unsafe-perm && \  
mv generator-chisel-*.tgz generator-chisel.tgz  
  
FROM ubuntu:18.04  
RUN groupadd --gid 1000 chisel \  
&& useradd --uid 1000 --gid chisel --shell /bin/bash --create-home chisel  
  
RUN apt-get update && \  
apt-get install -y php-cli php-mysql curl mysql-client && \  
rm -rf /var/lib/apt/lists/* && \  
php -v && \  
mysql --version  
  
COPY \--from=pack /generator-chisel/generator-chisel.tgz /generator-chisel/  
  
# Add Tini  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
USER chisel  
  
WORKDIR /home/chisel  
  
ENV N_PREFIX="/home/chisel/n" PREFIX="/home/chisel/n" \  
PATH="/home/chisel/n/bin:/home/chisel/bin:$PATH" \  
N_VERSION=2.1.8 NODE_VERSION=8 CHISEL_DOCKER=1  
RUN mkdir bin && \  
(curl -L "https://unpkg.com/n@$N_VERSION/bin/n" > ./bin/n) && \  
(echo '#!/bin/bash\n\nyo chisel "$@"' > ./bin/create) && \  
(echo '#!/bin/bash\n\nnpm run build "$@"' > ./bin/build) && \  
(echo '#!/bin/bash\n\nnpm run watch "$@"' > ./bin/watch) && \  
(echo '#!/bin/bash\n\nnpm run dev "$@"' > ./bin/dev) && \  
(echo '#!/bin/bash\n\nnpm run lint "$@"' > ./bin/lint) && \  
# (echo '#!/bin/bash\n\ntest -d wp && npx browser-sync start --port 2999
--proxy http://chisel-project/ --ws --no-ui; tail -f /dev/null' > ./bin/proxy)
&& \  
(echo '#!/bin/bash\n\ntail -f /dev/null' > ./bin/proxy) && \  
chmod +x ./bin/* && \  
n $NODE_VERSION && \  
npm install -g yarn yo && \  
yarn -v && \  
npm install -g /generator-chisel/generator-chisel.tgz && \  
npm cache clean --force && \  
mkdir -p /home/chisel/.cache/yarn && \  
mkdir -p /home/chisel/.npm/_cacache && \  
mkdir project  
  
VOLUME /home/chisel/.cache/yarn /home/chisel/.npm/_cacache  
  
WORKDIR /home/chisel/project  
EXPOSE 2999 3000  
CMD ["proxy"]  

