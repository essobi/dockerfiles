# https://hub.docker.com/_/node/  
FROM node:9-alpine  
  
RUN npm install -g yarn serve  
  
WORKDIR /app/  
  
# Create app  
#RUN npm install -g create-react-app \  
# && yarn config set init-author-name "David Luhmer" \  
# && yarn config set init-author-email "david.luhmer@smail.inf.h-brs.de" \  
# && yarn config set init-author-url "" \  
# && yarn config set init-version "1.0" \  
# && yarn config set init-license "MIT"  
#CMD /bin/sh -c "create-react-app . && yarn init --yes && yarn add react
react-dom"  
# Difference between ; and && in shell command: ; executes all of them. &&
only execute is previous was successful  
COPY package.json yarn.lock ./  
#RUN yarn install --frozen-lockfile --no-cache --production  
RUN yarn install --no-cache --production  
  
COPY . /app  
  
ARG NODE_ENV=production  
RUN set -ex; \  
if [ "$NODE_ENV" = "dev" ]; then \  
echo "Dev Environment"; \  
# elif [ "$NODE_ENV" = "test" ]; then \  
# yarn install --no-cache --frozen-lockfile; \  
else \  
echo "Production Environment" && \  
yarn build; \  
fi;  
  
CMD serve -s build --port 3000  
#CMD yarn start  
# Multi-Stage Build  
#FROM nginx  
#COPY --from=builder /app/build /usr/share/nginx/html

