# 1/2 Create build image  
FROM node:8.10-alpine AS build  
  
RUN mkdir -p /opt/link-proxy-web  
WORKDIR /opt/link-proxy-web  
  
COPY package.json yarn.lock ./  
RUN yarn --production  
  
# 2/2 Create production image  
FROM node:8-alpine  
ARG SOURCE_COMMIT=unknown  
  
RUN mkdir -p /opt/link-proxy-web  
WORKDIR /opt/link-proxy-web  
  
COPY \--from=build /opt/link-proxy-web .  
COPY . .  
  
ENV NODE_ENV=production \  
S3_ACCESS_KEY_FILE=s3_access_key \  
S3_SECRET_KEY_FILE=s3_secret_key \  
SENTRY_DSN_FILE=sentry_dsn \  
SENTRY_RELEASE=${SOURCE_COMMIT}  
  
RUN mkdir -p /opt/bin  
COPY docker/scripts/entrypoint.sh /opt/bin/  
  
EXPOSE 5000  
ENTRYPOINT ["/opt/bin/entrypoint.sh"]  
CMD ["yarn", "start:web"]  

