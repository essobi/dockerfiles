FROM nginx:alpine  
  
RUN apk -U add build-base fcgiwrap git libffi-dev ruby ruby-bundler ruby-dev
ruby-json \  
&& rm -f /var/cache/apk/* \  
&& gem install --clear-sources --no-document --no-rdoc jekyll -v '~> 3.7.0' \  
&& mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled  
  
COPY files/. /  
  
VOLUME /source /site  
  
ENTRYPOINT ["/entrypoint"]  
CMD ["/startup"]  

