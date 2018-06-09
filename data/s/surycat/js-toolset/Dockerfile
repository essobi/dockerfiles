FROM alpine:3.7  
ENV WORKSPACE /home/devuser  
ENV PATH $PATH:/home/devuser/.yarn/bin  
  
COPY settings/repositories /etc/apk/repositories  
# Installing build tools  
RUN apk --update add \  
bash \  
tar \  
git \  
nodejs \  
nodejs-npm \  
jq \  
curl \  
yarn  
  
RUN addgroup staff  
RUN adduser -D -g "" -G staff -s /bin/bash devuser  
RUN echo "devuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN touch ${WORKSPACE}/.bashrc  
RUN chown -R devuser:staff ${WORKSPACE}  
  
# Installing the JS toolchain  
RUN npm install -g bower  
RUN npm install -g gulp  
# Use `--unsafe-perm` to fix permission access:
https://github.com/npm/npm/issues/17851  
RUN npm install --unsafe-perm -g node-sass  
  
USER devuser  
WORKDIR ${WORKSPACE}

