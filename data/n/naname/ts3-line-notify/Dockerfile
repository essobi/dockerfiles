FROM node:6.10.2  
#RUN useradd --user-group --create-home --shell /bin/false app && \  
# npm install --global npm@4.5.0  
RUN useradd --user-group --create-home --shell /bin/false app  
RUN curl -0 -L https://npmjs.org/install.sh | sh # 3.10.10  
  
ENV HOME=/home/app  
  
COPY package.json npm-shrinkwrap.json $HOME/net/  
RUN chown -R app:app $HOME  
  
USER app  
WORKDIR $HOME/net  
RUN npm install  
CMD ["node", "src/index.js"]

