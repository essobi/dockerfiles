FROM alpine:3.7  
RUN apk update && apk upgrade && apk --update add \  
ruby ruby-irb ruby-rake ruby-io-console ruby-bigdecimal ruby-json ruby-bundler
\  
libstdc++ tzdata bash ca-certificates \  
less ncurses libssh2 libcurl expat pcre git \  
&& echo 'gem: --no-document' > /etc/gemrc && \  
gem install ghi && \  
apk del build-base  
ENTRYPOINT ["ghi"]  

