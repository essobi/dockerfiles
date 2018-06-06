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
RUN yarn install --production  
  
ENV PATH="/usr/src/collector/node_modules/.bin:${PATH}"  
# run everything from here on as non-root  
USER app  
  
ADD src /usr/src/collector/src  
RUN mkdir build && yarn run babel  
  
WORKDIR /repo  
  
ENTRYPOINT ["node", "--optimize_for_size", "--max_old_space_size=460",
"/usr/src/collector/build/entrypoint.js"]  
CMD ["/"]  

