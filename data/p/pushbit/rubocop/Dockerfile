FROM pushbit/ruby  
  
MAINTAINER Luke Roberts "email@luke-roberts.co.uk"  
RUN gem install rubocop  
RUN gem install faraday  
  
ADD ./execute.sh ./execute.sh  
ADD ./execute.rb ./execute.rb  
ADD ./rubocop.yml ./.rubocop.yml  
  
CMD ["./execute.sh"]

