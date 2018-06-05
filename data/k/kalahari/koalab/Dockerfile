FROM node:6  
ADD . /app  
WORKDIR /app  
RUN npm install --color false \--quiet --global grunt-cli bower \  
&& npm install --color false \--quiet \  
&& npm cache clean --color false \  
&& bower install --allow-root --no-color \  
&& grunt --no-color \  
&& mv config/server.json.docker /tmp/ \  
&& rm -rf config/* \  
&& mv /tmp/server.json.docker config/server.json  
EXPOSE 8080  
ENTRYPOINT [ "/usr/local/bin/node" ]  
CMD [ "./koalab.js" ]  

