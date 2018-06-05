FROM node:0.12  
RUN useradd node -u 1001 && mkdir /home/node && chown -R 1001:0 /home/node &&
npm install -g grunt-cli bower  
COPY ./s2i/bin/ /home/node/s2i/bin  
RUN chmod 0777 /home/node/s2i/bin/*  
LABEL io.openshift.s2i.scripts-url=image:///home/node/s2i/bin  
USER 1001  
WORKDIR /home/node  
CMD ["npm", "start"]

