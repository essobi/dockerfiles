FROM ruby:2.2.2  
MAINTAINER Joe Ferris <jferris@thoughtbot.com>  
RUN mkdir -p /opt/include  
RUN mkdir /src  
RUN mkdir /build  
RUN gem install sass  
RUN gem install bourbon -v 4.2.3  
RUN bourbon install --path /opt/include  
WORKDIR /src  
ENTRYPOINT ["sass", "--load-path", "/opt/include"]  
CMD ["--update", "/src:/build"]  

