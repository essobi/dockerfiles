FROM node:8  
# add a non-root user and give them ownership  
RUN useradd -u 9000 app && \  
# user home directory  
mkdir /home/app && \  
chown -R app:app /home/app && \  
# repo  
mkdir /repo && \  
chown -R app:app /repo && \  
# collector code  
mkdir -p /usr/src/app && \  
chown -R app:app /usr/src/app  
  
WORKDIR /usr/src/app  
ADD package.json /usr/src/app  
ADD yarn.lock /usr/src/app  
# install anything else we need  
RUN yarn install --production  
  
ENV PATH="/usr/src/app/node_modules/.bin:${PATH}"  
# add the deps utility to easily create pull requests on different git hosts  
ENV DEPS_VERSION=2.3.0  
RUN wget https://github.com/dependencies-
io/deps/releases/download/${DEPS_VERSION}/deps_${DEPS_VERSION}_linux_amd64.tar.gz
&& \  
mkdir deps && \  
tar -zxvf deps_${DEPS_VERSION}_linux_amd64.tar.gz -C deps && \  
ln -s /usr/src/app/deps/deps /usr/local/bin/deps  
  
# run everything from here on as non-root  
USER app  
  
RUN git config --global user.email "bot@dependencies.io"  
RUN git config --global user.name "Dependencies.io Bot"  
  
ADD src /usr/src/app/src  
RUN mkdir build && yarn run babel  
  
WORKDIR /repo  
  
ENV NODE_OPTIONS="--max_old_space_size=460"  
ENTRYPOINT ["node", "--optimize-for-size", "/usr/src/app/build/entrypoint.js"]  
CMD ["/"]  

