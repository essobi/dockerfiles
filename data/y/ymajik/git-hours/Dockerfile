FROM node:6-alpine  
  
LABEL maintainer=ymajik@gmail.com  
  
# org.label-schema.name = "ymajik/docker-git-hours" \  
# org.label-schema.description = "Git-hours is a tool to estimate time spent
on a git repository" \  
# org.label-schema.version="1.2.0" \  
# org.label-schema.vendor="ymajik" \  
# org.label-schema.docker.cmd="docker run --rm -v $(pwd):/code ymajik/git-
hours" \  
# org.label-schema.url="https://github.com/ymajik/docker-git-hours" \  
# org.label-schema.vcs-url="https://github.com/ymajik/docker-git-hours.git" \  
# org.label-schema.schema-version="1.0"  
RUN apk add --no-cache git libssh2 openssl-dev &&\  
rm -rf /var/cache/apk/*  
# Set unsafe perms when run as root, or, alternatively, run as a non-root user  
RUN npm init -y && \  
npm config set unsafe-perm true && \  
BUILD_ONLY=true npm install --save nodegit && \  
#npm install nodegit@0.15.1 && \  
npm prune --production && \  
npm install -g git-hours  
  
WORKDIR /code  
  
CMD git hours  

