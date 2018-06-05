FROM alpine:latest  
  
MAINTAINER Lindsay Evans <lindsay.evans@boomworks.com.au>  
  
ENV HOME=/home/app  
ENV PATH $PATH:/usr/lib/node_modules/bin  
  
# Add a user for npm to run under - prevents issues with permissions & so on  
RUN addgroup app && adduser -s /bin/bash -D -G app app  
  
RUN apk --no-cache add \  
abuild \  
bash \  
bash-completion \  
binutils \  
build-base \  
coreutils \  
gcc \  
nodejs \  
python  
  
# Show hostname in bash prompt & make things pretty colours  
RUN echo
"PS1='\\[\e[90m\\][\\[\e[36m\\]\h\\[\e[00m\\]\\[\e[90m\\]]\\[\e[00m\\] \$ '"
>> /home/app/.bashrc && \  
echo -e 'eval `dircolors -b`\nalias ls="ls --color=auto"\nalias l="ls
-lah"\nalias ll="ls -lh"' >> /home/app/.bashrc && \  
chown app:app /home/app/.bashrc  
  
# Install global NPM packages, congifure jspm for Bitbucket  
RUN npm install -g typescript typings grunt-cli gulp bower-installer jspm
jspm-git && \  
jspm config registries.bitbucket.baseurl ssh://git@bitbucket.org && \  
jspm config registries.bitbucket.handler jspm-git  
  
# Get our working directory up & running  
RUN mkdir /working  
# && chown app:app /working  
VOLUME /working  
WORKDIR /working  
  
# Run as app user  
#USER app  
# By default we run `npm install && npm start`  
# --no-bin-links is needed so that executable packages don't try to symlink in
our mounted volume, which causes issues on Windows  
CMD npm install --no-bin-links && npm start  

