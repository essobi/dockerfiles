FROM alpine:3.3  
MAINTAINER Erlend Finvåg <erlend@spiri.no>  
  
ENV GIT_DEPLOY_KEY=""  
ENV GIT_REMOTE=""  
ENV WEBHOOK_SECRET=""  
# Install prereqiusites  
RUN apk add --no-cache \  
ruby-unicorn ruby-json ruby-bundler ruby-io-console \  
git openssh-client su-exec  
  
# Create non-root user  
RUN adduser -D r10k  
  
# Disable ssh host key check as there is no shell to accept it in  
RUN echo "Host *" >> /etc/ssh/ssh_config && \  
echo " StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
  
# Install app  
COPY . /app  
WORKDIR /app  
RUN bundle install --without=test  
  
EXPOSE 8080  
VOLUME /var/cache/r10k # r10k cache  
VOLUME /etc/puppetlabs/code/environments # puppet environments  
  
ENTRYPOINT ["./entrypoint.sh"]  

