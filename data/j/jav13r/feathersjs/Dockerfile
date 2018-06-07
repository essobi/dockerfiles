FROM node:8.11.2-slim  
  
RUN apt-get update && apt-get install -y curl git && npm cache clean -f && \  
curl -o- -L https://yarnpkg.com/install.sh | bash && yarn global add \  
bower \  
grunt-cli \  
gulp-cli \  
grunt \  
rxjs \  
webpack \  
@feathersjs/cli  

