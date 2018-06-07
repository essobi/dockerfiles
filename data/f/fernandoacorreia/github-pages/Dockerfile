FROM ruby:2.1  
MAINTAINER Fernando de Alcântara Correia <fernando@fernandocorreia.info>  
  
RUN gem install \  
github-pages \  
therubyracer  
  
RUN github-pages versions  
  
EXPOSE 4000  
VOLUME /src  
WORKDIR /src  
CMD jekyll serve --drafts --baseurl ''  

