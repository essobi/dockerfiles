FROM ruby:2-stretch  
  
RUN apt-get -y update \  
&& apt-get -y install \  
libicu-dev \  
cmake \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem install \  
github-linguist \  
gollum \  
org-ruby \  
github-markdown  
  
WORKDIR /wiki  
  
ENTRYPOINT ["gollum", "--port", "4567"]  
  
EXPOSE 4567  

