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
mkdir -p /usr/src/collector && \  
chown -R app:app /usr/src/collector  
  
WORKDIR /usr/src/collector  
ADD package.json /usr/src/collector  
ADD yarn.lock /usr/src/collector  
# install anything else we need  
RUN yarn install  
  
# add lerna, our npm, and our yarn to the PATH  
ENV
PATH="/repo/node_modules/.bin:/usr/src/collector/node_modules/.bin:${PATH}"  
# run everything from here on as non-root  
USER app  
  
ADD entrypoint.js /usr/src/collector  
ADD collect.js /usr/src/collector  
  
WORKDIR /repo  
  
ENTRYPOINT ["node", "/usr/src/collector/entrypoint.js"]  
CMD ["/"]  

