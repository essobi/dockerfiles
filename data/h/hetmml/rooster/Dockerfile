FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y curl build-essential apt-transport-https  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs yarn  
  
COPY . /var/www  
WORKDIR /var/www  
  
RUN yarn  
RUN yarn build  
  
ENV PORT=80  
EXPOSE 80  
CMD yarn start  

