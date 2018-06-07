FROM node:alpine  
RUN apk upgrade -U && apk add python make g++ && \  
npm install -g kinesalite -q --unsafe-perm && \  
apk del make g++  
EXPOSE 4567  
CMD kinesalite ${USE_SSL:+--ssl} ${SHARD_LIMIT:+--shardLimit $SHARD_LIMIT}
${DB_PATH:+--path $DB_PATH}  

