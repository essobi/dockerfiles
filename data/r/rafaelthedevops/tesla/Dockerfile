FROM ubuntu:16.04  
FROM ruby:2.3.0  
MAINTAINER Rafael Monteiro <rafaelmonteiroti@gmail.com>  
  
EXPOSE 3000  
ENV HOME /home/rails/webapp  
  
RUN apt-get update -qq && apt-get install -y apt-utils  
RUN apt-get install -y build-essential libpq-dev nodejs  
  
RUN mkdir /railsapp  
  
WORKDIR $HOME  
  
ADD Gemfile* $HOME/  
RUN bundle install  
  
ADD . $HOME  
COPY entry.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entry.sh  
#Default command  
#CMD ["bin/bundle", "exec", "unicorn", "-p", "3000"]  
ENTRYPOINT ["/usr/local/bin/entry.sh"]  
CMD ["rails", "server", "--binding", "0.0.0.0"]  

