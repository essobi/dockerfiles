FROM ruby:2.3  
  
WORKDIR /var/www  
  
RUN groupadd -r gemstash \--gid=9999 && \  
useradd -r -g gemstash \--uid=9999 gemstash && \  
mkdir -p /home/gemstash/.gemstash && \  
mkdir -p /var/gemstash && \  
chown -R gemstash:gemstash /home/gemstash /var/gemstash  
  
USER gemstash  
  
ADD Gemfile* ./  
RUN bundle install  
  
ADD config.yml.erb /home/gemstash/.gemstash/  
  
#
https://github.com/bundler/gemstash/blob/6832d695e4b3a04d1452f7f84e3680e9632e69c7/lib/gemstash/cli/base.rb#L46  
# Otherwise, the pidfile will get created in the EFS, from both containers  
CMD ["bundle", "exec", "gemstash", "start", "--no-daemonize", "--pidfile",
"/home/gemstash/.gemstash/puma.pid"]  

