FROM bitwalker/alpine-elixir-phoenix:latest  
MAINTAINER Minh Tran <thminhkg@gmail.com>  
  
ENV APP_HOME /code  
RUN mkdir -p $APP_HOME  
WORKDIR $APP_HOME  
  
EXPOSE 4000  
CMD ["mix", "phx.server"]  

