FROM cardinalsoftwaresolutions/nginx-node-ruby-sass-compass  
  
COPY deploy/nginx.conf /etc/nginx/nginx.conf  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm set progress=false && npm install  
RUN mkdir -p /rx-more-cowbell-client && cp -a /tmp/node_modules /rx-more-
cowbell-client  
WORKDIR /rx-more-cowbell-client  
ADD . /rx-more-cowbell-client  
  
# Building dist  
RUN npm run build  
  
RUN ls -l  
  
# Copy dist to nginx for hosting  
RUN cp -a dist/. /usr/share/nginx/html

