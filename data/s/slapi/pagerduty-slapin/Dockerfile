FROM slapi/ruby:latest  
  
MAINTAINER SLAPI Devs  
  
LABEL "ack"="acknowledge incident"  
LABEL "create"="create items"  
LABEL "delete"="delete items"  
LABEL "help"="Describe available commands or one specific command"  
LABEL "list"="list items"  
LABEL "resolve"="resolve incident"  
LABEL "trigger"="trigger incident"  
LABEL "update"="update items"  
LABEL "version"="Get the version of the Pager Tool"  
  
RUN mkdir -p /pager && chmod 777 /pager  
WORKDIR /pager  
  
COPY .gemrc /root/.gemrc  
# Copy pager cli to container  
COPY . ./  
# Install dependencies  
RUN apk update &&\  
apk add ruby-dev &&\  
gem install io-console -v 0.4.5 &&\  
gem install bundler &&\  
bundle install &&\  
rm /var/cache/apk/*  
  
ENTRYPOINT ["/pager/bin/pager"]  

