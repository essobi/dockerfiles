FROM node:6.3  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y ruby-
compass vim-tiny libffi-dev build-essential libssl-dev && gem install
bootstrap-sass  
  
# /opt/ because we'll run from /opt/app/, and this puts node_modules upstream
of that.  
ADD package.json typings.json gulpfile.js tslint.json tsconfig.json /opt/  
  
# gotta install typings and gulp globally first (yeah, wtf)  
RUN cd /opt && npm install typings gulp -g \--color=false \--spin=false
\--progress=false \--loglevel=warn --unsafe-perm && npm install \--color=false
\--spin=false \--progress=false \--loglevel=warn --unsafe-perm && npm run
postinstall \--color=false \--spin=false \--progress=false \--loglevel=warn  
  
EXPOSE 3000  
CMD cd /opt/app && npm start  

