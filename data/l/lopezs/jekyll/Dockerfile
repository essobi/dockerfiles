FROM ruby:2.1  
MAINTAINER Lopez Shackleford <lopez.shackleford@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
node \  
python-pygments \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
RUN gem install \  
github-pages \  
jekyll \  
jekyll-redirect-from \  
kramdown \  
rdiscount \  
rouge \  
html-proofer  
  
VOLUME /src  
EXPOSE 4000  
WORKDIR /src  
  
ENTRYPOINT ["jekyll"]  
CMD ["serve", "-H", "0.0.0.0"]  

