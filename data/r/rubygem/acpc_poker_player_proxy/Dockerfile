FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.6.6  
RUN gem install acpc_poker_player_proxy --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["acpc_poker_player_proxy"]  
CMD ["--help"]  

