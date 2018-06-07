FROM dockerfile/nodejs-bower-grunt  
MAINTAINER jkremser  
  
RUN useradd -ms /bin/bash node  
ENV HOME /home/node  
#RUN npm install -g express && chown -R node /home/node/.npm  
USER node  
WORKDIR $HOME  
  
RUN git clone \--depth=1 https://github.com/Jiri-Kremser/25let.git  
WORKDIR 25let/25let-src  
RUN npm install && bower install && grunt build  
WORKDIR $HOME  
RUN mv 25let/25let-src/dist . && mv 25let/server.js . && rm -Rf 25let && npm
install express --save  
EXPOSE 3000  
ENTRYPOINT ["/usr/local/bin/node", "/home/node/server.js"]  
CMD []  

