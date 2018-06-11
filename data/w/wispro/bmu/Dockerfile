FROM ruby:2.4-alpine3.4  
RUN echo "gem: --no-rdoc --no-ri" >> ~/.gemrc && \  
apk --update add --virtual build-dependencies \  
build-base python && \  
apk --update add bash tzdata git openssh sqlite-dev nodejs rsync && \  
gem install bundler && \  
mkdir -m 700 -p /root/.ssh && \  
ssh-keyscan github.com >> ~/.ssh/known_hosts  
  
#RUN apk --update add libxml2 libxml2-dev libxml2-utils libxslt zlib  
WORKDIR /usr/src/app  
  
COPY .irbrc /root/.irbrc  
  
COPY Gemfile Gemfile.lock .keys/docker-rsa-utils .keys/docker-rsa-frontend
.keys/custom-git-ssh ./  
  
RUN chmod 600 docker-rsa-frontend docker-rsa-utils  
  
RUN GIT_SSH=/usr/src/app/custom-git-ssh bundle install --deployment --jobs 5 \  
&& apk del build-dependencies  
  
ADD . ./  
  
ENV RAILS_ENV=production  
  
RUN npm install -g yarn && yarn install && rails assets:precompile  
  
CMD ["/usr/src/app/bin/docker-cmd-server.sh"]  
  
EXPOSE 3000  

