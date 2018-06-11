FROM node:6.9.2  
MAINTAINER Sergey Popov <wailorman@gmail.com>  
  
# yarn  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  
  
RUN mkdir /ibb  
WORKDIR /ibb  
ADD ./package.json ./yarn.lock /ibb/  
RUN $HOME/.yarn/bin/yarn install --pure-lockfile  
ADD . /ibb  
  
#RUN npm run migrate  
EXPOSE 3000

