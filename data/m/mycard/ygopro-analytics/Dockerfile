FROM ruby  
  
# 安装 apt 依赖  
RUN apt-get update  
RUN apt-get install -y cron curl  
  
# 安装 ruby 依赖  
RUN bundle config --global frozen 1  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY ./Gemfile /usr/src/app  
COPY ./Gemfile.lock /usr/src/app  
RUN bundle install  
COPY . /usr/src/app  
  
# 设置时区  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# 配置计划任务  
COPY ./crontab /etc/crontab  
RUN crontab /etc/crontab  
  
# 卡片数据库  
# ADD https://mycard.moe/ygopro/cards.cdb Resources/cards.cdb  
# 启动  
CMD ["./entrypoint.sh"]  

