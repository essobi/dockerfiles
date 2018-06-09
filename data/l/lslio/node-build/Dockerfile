FROM node:alpine  
  
# Used for building sass-compass and similar.  
USER root  
RUN apk add \--update --no-cache tini make gcc g++ python git  
  
RUN yarn global add brunch  
  
USER node  
  
ENTRYPOINT ["tini", "--"]  
CMD ["node"]

