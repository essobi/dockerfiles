FROM tribalnova/alpine:latest  
MAINTAINER Nicolas Degardin <ndegardin@tribalnova.com>  
  
RUN adduser -D -s /bin/false -u 1000 node  
RUN mkdir -p /home/node/.npm && chown node -R /home/node/.npm && chown node
/srv  
  
ENV NPM_CONFIG_PREFIX="/home/node/.npm"  
RUN apk --update --no-cache add nodejs git make musl musl-utils openssh-client
jq libcap yarn  
RUN setcap cap_net_bind_service=+ep /usr/bin/node  
  
USER node  
ENV PATH="/home/node/.npm/bin:$PATH"  
RUN mkdir -p $HOME/.ssh && ssh-keyscan -H bitbucket.org >> ~/.ssh/known_hosts
&& ssh-keyscan -H github.com >> ~/.ssh/known_hosts  
RUN yarn global add grunt-cli gulp typescript gulp-typescript forever pm2
mocha newman force-dedupe-git-modules bunyan depcheck istanbul remap-istanbul
\  
browserify tsify vinyl-source-stream watchify gulp-util  
  
ADD files/startup.sh /opt/docker/startup.sh  
ADD files/build.sh /opt/docker/build.sh  
  
EXPOSE 80  
EXPOSE 5859  
WORKDIR /srv  
ENTRYPOINT ["/opt/docker/startup.sh"]  
CMD ["npm", "start"]  

