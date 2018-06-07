FROM ruby:2.4  
RUN mkdir /proyectoEventos  
WORKDIR /proyectoEventos  
  
ADD Gemfile /proyectoEventos/Gemfile  
ADD Gemfile.lock /proyectoEventos/Gemfile.lock  
  
RUN bundle install  
ADD . /proyectoEventos  

