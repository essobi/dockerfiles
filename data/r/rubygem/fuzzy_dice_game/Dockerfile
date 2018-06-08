FROM ruby:2.4  
MAINTAINER thinkbot@outlook.de  
  
ENV VERSION=1.5  
RUN gem install fuzzy_dice_game --version ${VERSION} \--no-format-exec  
  
WORKDIR /tmp  
  
ENTRYPOINT ["fuzzy_dice"]  
CMD ["--help"]  

