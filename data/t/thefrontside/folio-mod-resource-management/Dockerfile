FROM ruby:2.4.1  
RUN apt-get update -qq  
RUN mkdir /folio-mod-resource-management  
WORKDIR /folio-mod-resource-management  
ADD Gemfile /folio-mod-resource-management/Gemfile  
ADD Gemfile.lock /folio-mod-resource-management/Gemfile.lock  
RUN bundle install  
ADD . /folio-mod-resource-management  
EXPOSE 3000  
CMD ["rails", "server", "-b", "0.0.0.0"]  

