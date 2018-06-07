FROM eviles/alpine-sshd  
  
ENV NODE_ENV=production  
ENV GHOST_DIR=/usr/src/ghost  
ENV GHOST_CONTENT=/usr/src/ghost/content  
ENV PATH=$PATH:$GHOST_DIR/current/node_modules/knex-migrator/bin  
  
WORKDIR $GHOST_DIR  
  
RUN apk \--update add nodejs nodejs-npm make \  
&& npm install \--unsafe-perm -g ghost-cli \  
&& ghost install \--db sqlite3 \--no-prompt \--no-stack \--no-setup \--dir
"$GHOST_DIR" \  
&& ghost config \--ip 0.0.0.0 \--port 2368 \--no-prompt \--db sqlite3 \--url
http://localhost:2368 \--dbpath "$GHOST_CONTENT/data/ghost.db" \  
&& ghost config paths.contentPath "$GHOST_CONTENT" \  
&& knex-migrator-migrate \--init \--mgpath $GHOST_DIR/current \  
&& rm -rf /var/cache/apk/* \  
&& echo "[program:ghost]" >> /etc/supervisord.conf \  
&& echo "command=node $GHOST_DIR/current/index.js" >> /etc/supervisord.conf \  
&& echo "directory=$GHOST_DIR" >> /etc/supervisord.conf \  
&& echo "stdout_logfile=/dev/stdout" >> /etc/supervisord.conf \  
&& echo "stdout_logfile_maxbytes=0" >> /etc/supervisord.conf \  
&& echo "stderr_logfile=/dev/stderr" >> /etc/supervisord.conf \  
&& echo "stderr_logfile_maxbytes=0" >> /etc/supervisord.conf  
  
VOLUME $GHOST_CONTENT  
EXPOSE 2368  

