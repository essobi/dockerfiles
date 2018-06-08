FROM node:latest  
  
COPY ldap-server-mock-*.json /srv/  
  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
  
RUN su -c "npm install -g ldap-server-mock" node && \  
su -c "rm -rf /home/node/.npm" node  
EXPOSE 3004  
  
CMD ["node", "/home/node/.npm-global/lib/node_modules/ldap-server-
mock/server.js", "--conf=/srv/ldap-server-mock-conf.json", "--
database=/srv/ldap-server-mock-users.json"]  

