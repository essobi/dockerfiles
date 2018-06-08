# VERSION 1.0  
# AUTHOR: Jerome Guibert <jguibert@gmail.com>  
# DESCRIPTION: lilypond docker image  
# TO_BUILD: docker build --rm -t airdock/lilypond .  
# SOURCE: https://github.com/airdock-io/docker-lilypond  
FROM airdock/rvm:latest  
LABEL maintainer Jerome Guibert <jguibert@gmail.com>  
RUN apt-get update -qq && apt-get install -y cmake  
USER ruby  
RUN mkdir -p /srv/ruby/lilypond && cd /srv/ruby/lilypond && \  
rvm ruby-2.3 do gem install lyp --no-ri --no-rdoc && \  
rvm ruby-2.3 do lyp install lilypond && \  
rvm ruby-2.3 do lyp install lilyjazz  
USER root  
WORKDIR /srv/ruby/lilypond  
ENTRYPOINT ["tini", "-g", "--", "gosu", "ruby:ruby", "rvm", "ruby-2.3", "do",
"lilypond"]  

