FROM node:10 as builder  
LABEL maintainer="PurdueUSB <usb@cs.purdue.edu>"  
  
## Custom Stuff now ##  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y && apt-get install -y apt-transport-https  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -y && apt-get install -y --no-install-recommends yarn &&
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /app  
  
COPY ./package.json ./yarn.lock ./  
RUN yarn  
  
COPY ./backend/package.json ./backend/yarn.lock ./backend/  
RUN cd ./backend && yarn  
  
COPY . ./  
RUN yarn build && cp -r ./dist/* ./backend/public/  
  
# Multi Stage! #  
# The first stage builds everything from source  
# The second stage serves it  
FROM node:10  
LABEL maintainer="PurdueUSB <usb@cs.purdue.edu>"  
  
COPY \--from=builder /app/backend/ /app/openideas/  
  
ENV TINI_VERSION v0.18.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
EXPOSE 8081  
ENV NODE_ENV production  
  
WORKDIR /app/openideas  
# Use baseimage-docker's init process.  
CMD ["yarn", "start"]  

