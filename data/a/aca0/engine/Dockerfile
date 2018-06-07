FROM aca0/engine-deps:master  
  
COPY entrypoint.sh /entrypoint.sh  
  
# Workaround for https://github.com/moby/moby/issues/15858  
WORKDIR /home/aca-apps/ruby-engine-app  
COPY .gitignore Gemfile README.md Rakefile config.ru ./  
COPY .git ./.git/  
COPY app/ ./app/  
COPY bin/ ./bin/  
COPY config/ ./config/  
COPY db/ ./db/  
COPY lib/ ./lib/  
COPY log/ ./log/  
COPY modules/ ./modules/  
COPY public/ ./public/  
COPY test/ ./test/  
COPY tmp/ ./tmp/  
  
RUN chmod a+x /entrypoint.sh && \  
cp -f /usr/share/zoneinfo/Australia/Sydney /etc/localtime && \  
echo "Australia/Sydney" > /etc/timezone  
  
WORKDIR /home/aca-apps  
  
RUN git clone \--depth=1 --single-branch -b couchbase-orm
https://github.com/QuayPay/coauth.git /home/aca-apps/coauth && \  
git clone \--depth=1 https://github.com/acaprojects/ruby-engine.git && \  
git clone \--depth=1 https://github.com/acaprojects/aca-device-modules.git &&
\  
git clone \--depth=1 https://github.com/aca-labs/omniauth-jwt  
  
WORKDIR /home/aca-apps/ruby-engine-app  
RUN bundle update  
  
RUN apk del cmake && \  
rm -rf /var/cache/apk/*  
  
RUN echo "=====================================================" && \  
cat Gemfile.lock  
  
ENV RAILS_ENV=production DISABLE_SPRING=1 RAILS_LOG_TO_STDOUT=true  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["engine"]  

