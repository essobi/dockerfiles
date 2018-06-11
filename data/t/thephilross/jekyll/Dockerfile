# A static blog generator  
FROM ruby:2.1  
MAINTAINER philippross369@gmail.com  
  
RUN apt-get update \  
&& apt-get install -y \  
node \  
python-pygments \  
&& apt-get clean  
# && rm -rf /var/lib/apt/lists/  
RUN gem install \  
github-pages \  
jekyll \  
jekyll-redirect-from \  
kramdown \  
rdiscount \  
rouge  
  
COPY ./site_template/ /usr/local/bundle/gems/jekyll-3.0.1/lib/site_template  
  
VOLUME /src  
EXPOSE 4000  
WORKDIR /src  
ENTRYPOINT ["jekyll"]  

