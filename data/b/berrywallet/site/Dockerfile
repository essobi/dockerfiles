FROM node:9-wheezy  
  
LABEL version="0.1"  
LABEL description="BerryWallet Site Docker Image"  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64.deb && \  
dpkg -i dumb-init_*.deb && \  
rm -f dumb-init_*.deb  
  
WORKDIR /usr/src/berrywallet-site  
COPY . .  
  
ENV NODE_ENV=production  
ENV DB_HOST=localhost  
ENV DB_USER=postgres  
ENV DB_PASS=mysecretpassword  
ENV DB_NAME=berrywallet-site  
  
# install dev deps, build, rerun yarn to get rid of dev deps  
RUN yarn install --production=false && \  
npm run build:front:prod && \  
npm run build:server && \  
yarn install  
  
# remove source code  
RUN rm -rf \  
src \  
public \  
.cache-loader \  
webpack.config.js \  
tsconfig.json \  
tslint.json \  
postcss.config.js \  
gulpfile.babel.js \  
.babelrc \  
.browserslistrc \  
yarn.lock  
  
EXPOSE 3000  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["npm", "start"]  

