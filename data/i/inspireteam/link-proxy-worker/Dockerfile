# 1/2 Create build image  
FROM node:8.10-slim AS build  
  
RUN mkdir -p /opt/link-proxy-worker  
WORKDIR /opt/link-proxy-worker  
  
COPY package.json yarn.lock ./  
RUN yarn --production  
  
# 2/2 Create production image  
FROM node:8.10-slim  
ARG SOURCE_COMMIT=unknown  
  
RUN apt-get update -qq && \  
apt-get install -qq -y unar && \  
apt-get install -qq -y locales  
  
RUN locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
RUN mkdir -p /opt/link-proxy-worker  
WORKDIR /opt/link-proxy-worker  
  
COPY \--from=build /opt/link-proxy-worker .  
COPY . .  
  
ENV NODE_ENV=production \  
LC_ALL=C.UTF-8 \  
S3_ACCESS_KEY_FILE=s3_access_key \  
S3_SECRET_KEY_FILE=s3_secret_key \  
SENTRY_DSN_FILE=sentry_dsn \  
SENTRY_RELEASE=${SOURCE_COMMIT}  
  
RUN mkdir -p /opt/bin  
COPY docker/scripts/entrypoint.sh /opt/bin/  
  
ENTRYPOINT ["/opt/bin/entrypoint.sh"]  
CMD ["yarn", "start:worker"]  

