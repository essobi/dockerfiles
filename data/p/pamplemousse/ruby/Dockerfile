FROM ruby  
  
RUN gem install \  
awesome_print \  
colorize \  
pry pry-byebug \  
nokogiri \  
mechanize \  
rubocop \  
travis  
  
RUN useradd -m -u 1000 ruby  
WORKDIR /home/ruby  
USER ruby  
  
CMD ["pry"]  

