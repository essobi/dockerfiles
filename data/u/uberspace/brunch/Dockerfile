FROM node:alpine  
  
ARG NODE_ENV=development  
ENV NODE_ENV=$NODE_ENV \  
LOGGY_STACKS=1  
  
# Install build tools (needed for gyp)  
RUN apk add \--no-cache build-base git python  
  
# Setup user and working directories  
RUN set -ex; \  
DIRS="app public config"; \  
for DIR in ${DIRS}; do \  
mkdir "/home/node/${DIR}"; \  
chown node:node "/home/node/${DIR}"; \  
done;  
  
# Copy default configuration files to /tmp/default-config  
COPY config/package.json \  
config/yarn.lock \  
config/brunch-config.js \  
/tmp/default-config/  
  
# Setup configuration: copy defaults if needed and add link from home  
RUN set -ex; \  
CFGFILES="package.json yarn.lock brunch-config.js"; \  
for filename in ${CFGFILES}; do \  
filepath="/home/node/config/${filename}"; \  
if [ ! -f "${filepath}" ]; then \  
cp "/tmp/default-config/${filename}" "${filepath}"; \  
chown node:node "${filepath}"; \  
fi; \  
ln -s "${filepath}" "/home/node/${filename}"; \  
done;  
  
# Setup run environment  
USER node:node  
WORKDIR /home/node  
  
# Install default dependencies  
RUN yarn install  
  
# Setup starting environment  
EXPOSE 3333  
EXPOSE 9485  
ENTRYPOINT ["yarn", "run", "brunch"]  
CMD ["watch", "--server", "--network"]  

