  
FROM mhart/alpine-node:8.5  
  
RUN apk add --update --no-cache python \  
python-dev \  
py-pip \  
nano \  
make \  
gcc \  
g++ \  
git \  
&& rm -rf /var/cache/apk/* \  
&& pip install awscli  
  
RUN npm i @types/blueimp-md5 @types/body-parser @types/chalk @types/debug
@types/express \  
@types/fs-extra @types/redux auth0-lock auto-launch blueimp-md5 body-parser
bufferutil \  
chalk cloudant debug express fs-extra monaco-editor pug redux socket.io
typescript-react-intl \  
utf-8-validate uuidgen @types/express @types/gulp-util @types/jsdom
@types/pubsub-js \  
@types/react @types/react-router @types/source-map-support @types/xtend
bootstrap browserify \  
browserify-incremental cli-spinner colortape cross-env del enzyme fs-extra
g11n-pipeline \  
glob gulp gulp-clean-dest gulp-cssnano gulp-duration gulp-notify gulp-
preprocess gulp-sass \  
gulp-sourcemaps gulp-tape gulp-tslint gulp-typescript gulp-uglify gulp-util
gulp-watch \  
history jsdom moment-timezone nodemon nop optional pouch-redux-middleware
pouchdb-find \  
pouchdb-mc pouchdb-upsert pubsub-js react react-addons-css-transition-group
react-addons-test-utils \  
react-addons-transition-group react-audio-player react-dom react-id-swiper \  
react-intl react-redux react-router react-superagent reactstrap redux require-
dir \  
retyped-socket.io-client-tsd-ambient run-sequence socket.io-client socket.io-
react \  
source-map-support superagent tap-colorize tape tsify tslint tslint-react
typescript \  
vinyl-buffer vinyl-paths vinyl-source-stream xtend \  
&& mv node_modules /prebuilt-modules  

