FROM node:8.6  
ENV NODE_ENV production  
WORKDIR /usr/src/app  
COPY ["package.json", "npm-shrinkwrap.json*","install.bash", "./"]  
RUN chmod +X install.bash  
RUN ./install.bash  
RUN npm install --production #&& mv node_modules ../  
COPY . .  
ENTRYPOINT luminati

