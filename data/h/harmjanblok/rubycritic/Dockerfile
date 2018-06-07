FROM ruby:2.4  
ENV HOME /rubycritic  
WORKDIR ${HOME}  
  
ADD Gemfile Gemfile.lock ${HOME}/  
RUN bundle install --jobs 4  
  
RUN chown -R nobody:nogroup ${HOME}  
USER nobody  
  
WORKDIR /usr/src/app  
  
CMD ["rubycritic", "--no-browser"]  

