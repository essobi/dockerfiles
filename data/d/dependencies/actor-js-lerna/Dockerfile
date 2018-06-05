FROM node:8  
# add a non-root user and give them ownership  
RUN useradd -u 9000 app && \  
# user home directory  
mkdir /home/app && \  
chown -R app:app /home/app && \  
# repo  
mkdir /repo && \  
chown -R app:app /repo && \  
# actor code  
mkdir /usr/src/actor && \  
chown -R app:app /usr/src/actor  
  
WORKDIR /usr/src/actor  
  
ADD package.json /usr/src/actor  
ADD yarn.lock /usr/src/actor  
RUN yarn install  
  
# add lerna to the PATH  
ENV PATH="/repo/node_modules/.bin:/usr/src/actor/node_modules/.bin:${PATH}"  
# add the pullrequest utility to easily create pull requests on different git
hosts  
ENV PULLREQUEST_VERSION=0.6.0  
RUN wget https://github.com/dependencies-
io/deps/releases/download/${PULLREQUEST_VERSION}/pullrequest_${PULLREQUEST_VERSION}_linux_amd64.tar.gz
&& \  
mkdir pullrequest && \  
tar -zxvf pullrequest_${PULLREQUEST_VERSION}_linux_amd64.tar.gz -C pullrequest
&& \  
ln -s /usr/src/actor/pullrequest/pullrequest /usr/local/bin/pullrequest  
  
# run everything from here on as non-root  
USER app  
  
RUN git config --global user.email "bot@dependencies.io"  
RUN git config --global user.name "Dependencies.io Bot"  
  
ADD entrypoint.js /usr/src/actor  
  
WORKDIR /repo  
  
ENTRYPOINT ["node", "--optimize_for_size", "--max_old_space_size=460",
"/usr/src/actor/entrypoint.js"]  

