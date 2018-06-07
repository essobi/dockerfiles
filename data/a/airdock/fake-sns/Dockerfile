# VERSION 1.0  
# AUTHOR: Jerome Guibert <jguibert@gmail.com>  
# DESCRIPTION: Fake SNS image based on airdock/rvm  
# TO_BUILD: docker build --rm -t airdock/fake-sns .  
# SOURCE: https://github.com/airdock-io/docker-fake-sns  
FROM airdock/rvm:latest  
LABEL maintainer Jerome Guibert <jguibert@gmail.com>  
  
USER ruby  
  
RUN mkdir -p /srv/ruby/fake-sns && cd /srv/ruby/fake-sns && \  
rvm ruby-2.3 do gem install fake_sns --no-ri --no-rdoc  
  
USER root  
  
EXPOSE 9292  
  
VOLUME ["/srv/ruby/fake-sns"]  
  
CMD ["tini", "-g", "--", "gosu", "ruby:ruby", "rvm", "ruby-2.3", "do",
"fake_sns", "--database", "/srv/ruby/fake-sns/database.yml", "-p", "9292"]  

