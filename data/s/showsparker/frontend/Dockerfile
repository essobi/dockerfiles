FROM ubuntu:17.04  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN echo "\  
deb http://us-central1.gce.archive.ubuntu.com/ubuntu/ zesty main restricted
universe multiverse\n\  
deb http://us-central1.gce.archive.ubuntu.com/ubuntu/ zesty-updates main
restricted universe multiverse\n\  
deb http://us-central1.gce.archive.ubuntu.com/ubuntu/ zesty-backports main
restricted universe multiverse\n\  
" > /etc/apt/sources.list  
RUN apt-get update && apt-get install --yes --no-install-recommends curl ca-
certificates apt-transport-https  
RUN echo "\  
deb https://deb.nodesource.com/node_7.x yakkety main\n\  
deb-src https://deb.nodesource.com/node_7.x yakkety main\n\  
deb https://dl.yarnpkg.com/debian/ stable main\n\  
" >> /etc/apt/sources.list  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-
key add -  
RUN apt-get update  
RUN apt-get install --yes --no-install-recommends nodejs yarn  
  
RUN useradd -ms /bin/bash showsparker  
  
ADD package.json /home/showsparker/showsparker-frontend/  
ADD yarn.lock /home/showsparker/showsparker-frontend/  
RUN chown -R showsparker. /home/showsparker/  
  
USER showsparker  
WORKDIR /home/showsparker/showsparker-frontend/  
  
RUN yarn install  
  
ADD . /home/showsparker/showsparker-frontend/  
USER root  
RUN chown -R showsparker. /home/showsparker/  
USER showsparker  
  
EXPOSE 8000  
CMD ["yarn", "run", "start"]  

