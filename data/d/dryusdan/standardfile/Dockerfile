FROM node:6-alpine  
  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc \  
&& apk -U upgrade \  
&& apk add -t build-dependencies \  
git \  
curl-dev \  
wget \  
ruby-dev \  
zlib-dev \  
build-base \  
mariadb-dev \  
&& apk add ruby ruby-io-console ruby-json ruby-bigdecimal zlib tzdata mariadb-
client-libs \  
&& gem install -N rails --version "$RAILS_VERSION" \  
&& echo 'gem: --no-document' >> ~/.gemrc \  
&& cp ~/.gemrc /etc/gemrc \  
&& chmod uog+r /etc/gemrc \  
&& npm install -g bower \  
&& rm -rf ~/.gem \  
&& git clone https://github.com/standardfile/ruby-server.git standardfile \  
&& cd standardfile \  
&& rm -rf .git/ \  
&& gem install bigdecimal \  
&& echo "bundle install" \  
&& bundle config --global silence_root_warning 1 \  
&& bundle install --system \  
&& echo "bower install" \  
&& bower install --allow-root \  
&& apk del build-dependencies \  
&& rm -rf /tmp/* /var/cache/apk/* /tmp/* /root/.gnupg /root/.cache/ \  
&& echo "bundle precompile" \  
&& bundle exec rake assets:precompile  
  
EXPOSE 3000  
COPY /docker /docker  
  
ENTRYPOINT [ "/docker/entrypoint" ]  
CMD [ "start" ]  

