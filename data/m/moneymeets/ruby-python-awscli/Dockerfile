FROM alpine:3.7  
  
RUN set -ex \  
&& apk add --update --no-cache \  
python3 \  
&& pip3 install --upgrade pip awscli requests \  
&& rm -r /root/.cache  
  
RUN set -ex \  
&& apk add --update --no-cache \  
build-base \  
git \  
libffi-dev \  
openssh \  
rsync \  
ruby \  
ruby-json \  
ruby-dev \  
ruby-rdoc \  
ruby-irb \  
ruby-bundler \  
zlib-dev  
  
CMD ["/bin/sh"]  

