FROM patricol/ubuntu_x11:18.04  
USER root  
  
RUN su user -c "umake nodejs /home/user/.local/share/umake/nodejs/nodejs-lang"
&& \  
su user -c "umake ide webstorm /home/user/.local/share/umake/ide/webstorm"  
ENV NODE_PATH=/home/user/.local/share/umake/nodejs/nodejs-
lang/lib/node_modules:/home/user/.local/share/umake/nodejs/nodejs-
lang:/home/user/.local/share/umake/nodejs/nodejs-
lang/bin:/home/user/.npm_modules/lib/node_modules:/home/user/.npm_modules/bin  
ENV PATH=$NODE_PATH:$PATH  
  
EXPOSE 3000 5000 9000  
  
RUN npm install -g npm@latest && \  
npm install --unsafe-perm -g gulp bower grunt grunt-cli yeoman-generator yo
generator-angular generator-karma generator-webapp  
  
USER user

