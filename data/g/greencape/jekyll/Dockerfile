FROM ruby:2.1  
MAINTAINER Niels Braczek <nbraczek@bsds.de>  
  
RUN apt-get update \  
&& apt-get install -y \  
node \  
python-pygments \  
&& apt-get clean  
  
COPY Gemfile /Gemfile  
  
RUN gem install bundler \  
&& bundle install --gemfile=/Gemfile  
  
VOLUME /src  
EXPOSE 4000  
WORKDIR /src  
ENTRYPOINT ["jekyll"]  
  

