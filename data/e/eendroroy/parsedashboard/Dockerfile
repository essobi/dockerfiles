FROM node:argon-slim  
  
MAINTAINER indrajit  
  
RUN apt-get update && \  
apt-get install unzip && \  
rm -rf /var/cache/apt/  
  
WORKDIR /tmp  
  
RUN wget https://github.com/parse-community/parse-dashboard/archive/master.zip
&& \  
unzip master.zip && \  
rm -rf .git .github .dockerignore .eslintrc.json .gitignore .travis.yml \  
CHANGELOG.md CONTRIBUTING.md Dockerfile README.md && \  
mkdir -p /src && mv parse-dashboard-master/* /src/  
  
WORKDIR /src  
  
RUN npm install && npm run build && npm cache clear && rm -rf ~/.npm  
  
ENV NPM_CONFIG_LOGLEVEL error  
  
WORKDIR /src  
  
ENTRYPOINT ["npm", "run", "dashboard"]

