FROM
yolean/node@sha256:c56ca739040c3bcab5e59b9c1072628ddd2de2707fa15b51b51c18c002750931  
  
ENV NODE_PATH=/usr/local/lib/node_modules  
  
RUN npm install -g \  
mocha@4.0.1 \  
chai@4.1.2 \  
request@2.83.0 \  
kubernetes-client@3.16.0  
  
WORKDIR /  
ENTRYPOINT [ "mocha", "--watch" ]

