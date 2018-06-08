FROM ruby:2.2.2  
MAINTAINER qhwa <qhwa@pnq.cc>  
  
# 使用阿里云源  
# ADD rc/sources.list.jessie /etc/apt/sources.list  
  
# postgresql-client 初始化的时候需要  
RUN apt-get update && apt-get install postgresql-client -y  
  
# 使用淘宝源加快速度  
RUN bundle config mirror.https://rubygems.org https://ruby.taobao.org  
RUN bundle config mirror.http://rubygems.org https://ruby.taobao.org  
  
##########################################################  
# mirrors  
##########################################################  
RUN echo 'gem: --no-rdoc --no-ri' >> $HOME/.gemrc  
ADD rubygems-mirror/Gemfile /app/rubygems-mirror/Gemfile  
ADD rubygems-mirror/Gemfile.lock /app/rubygems-mirror/Gemfile.lock  
RUN cd /app/rubygems-mirror && bundle install  
ADD rubygems-mirror /app/rubygems-mirror  
ADD mirrorrc /root/.gem/.mirrorrc  
ADD cron /app/cron  
# CMD ["bundle", "exec", "rake", "mirror:update"]  
  
##########################################################  
# bundler api  
##########################################################  
ENV APP=bundler-api  
ENV PORT=6000  
EXPOSE ${PORT}  
  
ADD ${APP}/Gemfile /app/${APP}/Gemfile  
ADD ${APP}/Gemfile.lock /app/${APP}/Gemfile.lock  
  
WORKDIR /app/${APP}  
  
# 修改了项目文件，但是没有修改 Gemfile 的情况下  
# 可以不需要重新 `bundle install`  
RUN bundle install  
  
ADD ${APP} /app/${APP}  
  
WORKDIR /app/${APP}  
RUN echo '' > .env  
  
# -- environments  
ENV RACK_ENV=development \  
MIN_THREADS=10 \  
MAX_THREADS=32 \  
REDIS_ENV=REDIS_URL \  
# link redis  
REDIS_URL=redis://redis:6379 \  
# link memcached  
MEMCACHE_SERVERS=cache:11211 \  
MEMCACHIER_SERVERS=cache:11211 \  
# link postgres  
DATABASE_URL=postgres://postgres@postgres/bundler-api \  
FOLLOWER_DATABASE_URL=postgres://postgres@postgres/bundler-api \  
TEST_DATABASE_URL=postgres://postgres@postgres/bundler-api-test \  
#  
RUBYGEMS_HOST=http://rubygems-china.oss.aliyuncs.com \  
DOWNLOAD_BASE=http://rubygems-china.oss.aliyuncs.com  
  
CMD ["bundle", "exec", "script/web"]  

