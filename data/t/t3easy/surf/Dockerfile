FROM composer  
  
ENV SURF_VERSION dev-master  
  
ENV PATH
"/tmp/vendor/bin:/root/.yarn/bin:/usr/local/share/.config/yarn/global/node_modules/.bin:$PATH"  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_CACHE_DIR /tmp/cache/composer  
ENV YARN_CACHE_FOLDER /tmp/cache/yarn  
ENV npm_config_cache /tmp/cache/npm  
  
# Install TYPO3 Surf  
RUN mkdir /tmp/cache && chmod -R 777 /tmp/cache  
  
RUN composer global require typo3/surf:${SURF_VERSION} && \  
composer clear-cache  
  
# Install build tools  
RUN apk --no-cache add \  
gnupg \  
nodejs \  
nodejs-npm \  
rsync \  
&& \  
curl -o- -L https://yarnpkg.com/install.sh | bash && \  
apk del gnupg  
  
RUN yarn global add gulp-cli && yarn cache clean  
  
# Configure ssh client  
COPY ssh_config /etc/ssh/ssh_config  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["surf"]  

