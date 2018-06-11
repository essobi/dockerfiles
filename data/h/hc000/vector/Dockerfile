FROM phusion/baseimage:0.9.17  
RUN apt-get update  
RUN apt-get install -y nodejs npm git && \  
ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g bower  
RUN sudo npm install http-server -g  
  
RUN git clone https://github.com/netflix/vector.git && \  
cd vector && \  
git checkout f2f65601713186236e07a4a156d4263dcf436540  
  
RUN cd vector/src/app/ && \  
sed -i '31s/false/true/' app.config.js  
  
RUN cd vector && \  
bower --allow-root install --config.interactive=false && \  
npm install && \  
npm install --global gulp && \  
gulp  
  
EXPOSE 33100:33100  
ENTRYPOINT ( cd vector/dist && http-server --cors -p 33100 )  

