#  
# Conjur-Cli Dockerfile  
#  
# https://github.com/deny4ll/deny4ll-docker-conjur-cli  
#  
#  
FROM alpine:3.5  
RUN apk update && apk upgrade && apk --update add \  
ruby ruby-irb ruby-rake ruby-io-console ruby-bigdecimal ruby-json ruby-bundler
\  
libstdc++ tzdata bash ca-certificates gcc make \  
&& echo 'gem: --no-document' > /etc/gemrc  
  
RUN apk --update add ruby-dev g++  
  
RUN gem install conjur-cli --version "=5.6.4"  
  
RUN apk --update add openssh-client  
  
# Define default command.  
CMD ["/bin/bash"]  

