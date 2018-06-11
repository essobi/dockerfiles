FROM buildpack-deps:jessie  
  
RUN set -ex; \  
groupadd --gid 1000 node; \  
useradd --uid 1000 --gid node --shell /bin/bash --create-home node; \  
\  
git clone https://github.com/facebook/watchman.git; \  
cd watchman; \  
git checkout v4.9.0; \  
./autogen.sh; \  
./configure --without-python; \  
make; \  
make install; \  
cd ..; \  
rm -Rf watchman  
  
USER node  
ENV HOME /home/node  
WORKDIR $HOME  
  
ENV NODE_VERSION v6.12.3  
ENV NVM_DIR $HOME/.nvm  
ENV YARN_DIR $HOME/.yarn  
  
RUN set -ex; \  
env; \  
mkdir -p ${NVM_DIR}  
  
COPY ./nvm.sh .  
COPY ./install-yarn.sh .  
  
RUN [ -s "${HOME}/nvm.sh" ] && . "${HOME}/nvm.sh"; \  
nvm install --lts=boron; \  
. "${HOME}/install-yarn.sh"  
  
ENV NVM_BIN ${NVM_DIR}/versions/node/${NODE_VERSION}/bin  
ENV YARN_BIN ${YARN_DIR}/bin  
ENV PATH ${NVM_BIN}:${YARN_BIN}:${PATH}  
  
CMD ["bash"]  

