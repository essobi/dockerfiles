# Pull base image  
FROM node:6  
  
#https://forums.couchbase.com/t/cannot-make-couchbase-node-js-sdk-working-
under-cenos-6-5/1128  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get -y install build-essential g++ logrotate cron less  
RUN npm install -g yarn  
RUN yarn global add node-gyp@latest apollo-client@0.5.6 apollo-server@0.3.3
apollo-server@0.3.3 babel-runtime@6.11.6 bcrypt@0.8.7 bluebird@3.4.6 browser-
bunyan@0.4.0 bunyan@1.8.1 chokidar@1.6.1 co@4.6.0 couchbase@2.3.0
dataloader@1.2.0 es6-promise@4.0.5 exit-hook@1.1.1 fs-extra@0.30.0
graphql@0.8.2 graphql-custom-datetype@0.3.0 graphql-relay@0.4.4 graphql-
tag@0.1.17 graphql-tools@0.8.4 graphql-type-json@0.1.4 handlebars@4.0.6
history@4.2.0 http-shutdown@1.0.3 install@0.8.1 isomorphic-fetch@2.2.1 json-
stringify-safe@5.0.1 jsonwebtoken@7.1.9 kcors@2.1.1 koa@2.0.0-alpha.7 koa-
better-body@2.0.1 koa-better-static@1.0.5 koa-compress@2.0.0 koa-convert@1.2.0
koa-mount@2.0.0 koa-router@7.0.1 lodash@4.15.0 mobx@2.6.3 mobx-react@4.0.3
npm@3.10.8 object-assign@4.1.0 react@15.3.2 react-dom@15.3.2 react-
motion@0.4.5 react-native-web@0.0.60 socket.io@1.7.1 tcomb-validation@3.3.0
unirest@0.5.1 url-pattern@1.0.1 uuid@3.0.0 webpack-node-externals@1.5.4
source-map-support@0.4.2 resolve-pathname@2.0.2 value-equal@0.1.1 babel-
cli@6.16.0 babel-core@6.17.0 babel-eslint@7.0.0 babel-loader@6.2.5 babel-
plugin-lodash@3.2.8 babel-plugin-module-resolver@2.3.0 babel-plugin-mobx-deep-
action@1.3.0 babel-plugin-module-resolver@2.4.0 babel-plugin-syntax-async-
functions@6.13.0 babel-plugin-transform-decorators-legacy@1.3.4 babel-plugin-
transform-flow-strip-types@6.14.0 babel-plugin-transform-regenerator@6.16.1
babel-plugin-transform-runtime@6.15.0 babel-preset-es2015@6.16.0 babel-preset-
react@6.16.0 babel-preset-stage-0@6.16.0 babel-preset-stage-2@6.17.0
concurrently@2.2.0 css-loader@0.24.0 del@2.2.2 elapsed-time@0.0.1 enzyme@2.4.1
fbjs@0.9.0-alpha.1 fbjs-scripts@0.6.0-alpha.3 json-loader@0.5.4 koa-webpack-
middleware@1.0.1 loader-utils@0.2.16 lodash-webpack-plugin@0.10.0 mkdirp@0.5.1
node-dir@0.1.16 node-sass@3.9.0 react-addons-test-utils@15.3.2 rimraf@2.5.4
sass-loader@4.0.1 source-map-explorer@1.3.2 style-loader@0.13.1 unlazy-
loader@0.1.2 url-loader@0.5.7 webpack@2.1.0-beta.25 webpack-manifest-
plugin@1.0.1 webpack-node-externals@1.4.3  
  
# Fix bug https://github.com/npm/npm/issues/9863  
# RUN cd $(npm root -g)/npm \  
# && npm install fs-extra \  
# && sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
#RUN npm install -g npm@latest && cd /root  
#RUN npm install -g node-gyp@latest apollo-client@0.5.6 apollo-server@0.3.3
apollo-server@0.3.3 babel-runtime@6.11.6 bcrypt@0.8.7 bluebird@3.4.6 browser-
bunyan@0.4.0 bunyan@1.8.1 chokidar@1.6.1 co@4.6.0 couchbase@2.2.4
dataloader@1.2.0 es6-promise@4.0.5 exit-hook@1.1.1 fs-extra@0.30.0
graphql@0.8.2 #graphql-custom-datetype@0.3.0 graphql-relay@0.4.4 graphql-
tag@0.1.17 graphql-tools@0.8.1 handlebars@4.0.6 history@4.2.0 http-
shutdown@1.0.3 install@0.8.1 isomorphic-fetch@2.2.1 json-stringify-safe@5.0.1
jsonwebtoken@7.1.9 kcors@2.1.1 koa@2.0.0-alpha.7 koa-better-body@2.0.1 koa-
better-static@1.0.5 #koa-compress@2.0.0 koa-convert@1.2.0 koa-mount@2.0.0
lodash@4.15.0 mobx@2.6.3 mobx-react@4.0.3 npm@3.10.8 object-assign@4.1.0
react@15.3.2 react-dom@15.3.2 react-motion@0.4.5 react-native-web@0.0.53 koa-
router@7.0.1 socket.io@1.7.1 tcomb-validation@3.3.0 unirest@0.5.1 url-
pattern@1.0.1 #webpack-node-externals@1.5.4  
#RUN npm install -g node-gyp@latest apollo-client@0.5.6 apollo-server@0.3.3
apollo-server@0.3.3 babel-runtime@6.11.6 bcrypt@0.8.7 bluebird@3.4.6 browser-
bunyan@0.4.0 bunyan@1.8.1 chokidar@1.6.1 co@4.6.0 couchbase@2.2.4
dataloader@1.2.0 es6-promise@4.0.5 exit-hook@1.1.1 fs-extra@0.30.0
graphql@0.8.2 #graphql-custom-datetype@0.3.0 graphql-relay@0.4.4 graphql-
tag@0.1.17 graphql-tools@0.8.1 handlebars@4.0.6 history@4.2.0 http-
shutdown@1.0.3  
#RUN npm install -g install@0.8.1 isomorphic-fetch@2.2.1 json-stringify-
safe@5.0.1 jsonwebtoken@7.1.9 kcors@2.1.1 koa@2.0.0-alpha.7 koa-better-
body@2.0.1 koa-better-static@1.0.5 koa-compress@2.0.0 koa-convert@1.2.0  
#RUN npm install -g koa-mount@2.0.0 lodash@4.15.0 mobx@2.6.3 mobx-react@4.0.3
npm@3.10.8 object-assign@4.1.0 react@15.3.2 react-dom@15.3.2 react-
motion@0.4.5 react-native-web@0.0.53  
#RUN npm install -g koa-router@7.0.1  
#RUN npm install -g socket.io@1.7.1  
#RUN npm install -g tcomb-validation@3.3.0 unirest@0.5.1 url-pattern@1.0.1
webpack-node-externals@1.5.4  
  
#RUN /usr/sbin/update-rc.d cron defaults  
  
ENV NODE_PATH /root/.config/yarn/global/node_modules  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD [bash]

