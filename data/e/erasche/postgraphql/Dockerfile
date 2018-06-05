FROM node:alpine  
MAINTAINER E Rasche <hxr@hx42.org>  
  
RUN apk update && \  
apk add postgresql-client postgresql git bash patch && \  
git clone https://github.com/calebmer/postgraphql/ /app/ && \  
cd /app && \  
git checkout a88a9836722c5d42c7cae93fe901c095d7c704f6 && \  
git config --global user.email "root@localhost" && \  
npm install  
  
ADD ugly.patch /ugly.patch  
ADD 0001-shutup.patch /bad.patch  
  
RUN cd /app && \  
git am /bad.patch && \  
patch /app/node_modules/graphql/type/schema.js < /ugly.patch && \  
npm run build  
  
USER nobody  
  
ADD run.sh /run.sh  
EXPOSE 5000  
ENTRYPOINT ["/run.sh"]  

