# Build image  
FROM node:10-alpine AS builder  
  
RUN apk --update add ruby imagemagick ca-certificates git && \  
apk --update add \--virtual sass-dev build-base ruby-dev libffi-dev && \  
gem install -N sass  
  
ENV APP_USER=3dptools  
  
RUN adduser -D -g "" -G users $APP_USER  
  
COPY src /3dptools  
COPY CHANGELOG.md /3dptools/CHANGELOG.md  
COPY docker/docker_start.sh /docker_start.sh  
RUN chown -R $APP_USER:users /docker_start.sh /3dptools && chmod +x
/docker_start.sh  
  
WORKDIR /3dptools  
  
RUN apk --update add \--virtual 3dpt-dev build-base python krb5-dev sudo && \  
sudo -u $APP_USER yarn install --production && \  
sudo -u $APP_USER yarn cache clean --force  
  
USER $APP_USER  
RUN yarn run bower install --production && \  
yarn run bower cache clean  
RUN scss -C -f public/stylesheets/style.scss public/stylesheets/style.css  
  
# Real image  
FROM node:10-alpine  
  
LABEL maintainer="Olivier Robardet <olivier.robardet@gmail.com>"  
  
ENV APP_USER=3dptools  
  
RUN adduser -D -g "" -G users $APP_USER  
  
COPY \--from=builder /3dptools /3dptools  
COPY docker/docker_start.sh /docker_start.sh  
RUN chown -R $APP_USER:users /3dptools /docker_start.sh && chmod +x
/docker_start.sh  
  
USER $APP_USER  
WORKDIR /3dptools  
  
ENV PORT=3000  
ENV NODE_ENV=production  
  
ENV database__host=mongo  
ENV redis__host=redis  
ENV sentry__dsn="https://88009fc2f595471ea9808336a43e42cd@sentry.io/148531"  
  
EXPOSE $PORT  
  
CMD ["/docker_start.sh"]

