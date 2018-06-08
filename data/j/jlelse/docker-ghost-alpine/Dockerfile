FROM alpine:3.7  
ENV NODE_ENV production  
ENV GHOST_CLI_VERSION 1.8.0  
ENV GHOST_VERSION 1.23.1  
ENV GHOST_INSTALL /var/lib/ghost  
ENV GHOST_CONTENT /var/lib/ghost/content  
  
RUN apk upgrade --no-cache; \  
apk add --no-cache nodejs nodejs-npm bash su-exec shadow; \  
npm install -g "ghost-cli@$GHOST_CLI_VERSION"; \  
useradd node; \  
mkdir -p "$GHOST_INSTALL"; \  
chown node "$GHOST_INSTALL"; \  
su-exec node ghost install "$GHOST_VERSION" \--db sqlite3 --no-prompt --no-
stack --no-setup --dir "$GHOST_INSTALL"; \  
cd "$GHOST_INSTALL"; \  
su-exec node ghost config --ip 0.0.0.0 --port 2368 --no-prompt --db sqlite3
--url http://localhost:2368 --dbpath "$GHOST_CONTENT/data/ghost.db"; \  
su-exec node ghost config paths.contentPath "$GHOST_CONTENT"; \  
su-exec node ln -s config.production.json
"$GHOST_INSTALL/config.development.json"; \  
mv "$GHOST_CONTENT" "$GHOST_INSTALL/content.orig"; \  
mkdir -p "$GHOST_CONTENT"; \  
chown node "$GHOST_CONTENT"; \  
"$GHOST_INSTALL/current/node_modules/knex-migrator/bin/knex-migrator"
\--version  
  
ENV PATH $PATH:$GHOST_INSTALL/current/node_modules/knex-
migrator/bin:/usr/local/bin  
  
WORKDIR $GHOST_INSTALL  
VOLUME $GHOST_CONTENT  
  
COPY docker-entrypoint.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 2368  
CMD ["node", "current/index.js"]  

