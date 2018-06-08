FROM jekyll/jekyll:3.4.0  
MAINTAINER Tobias Wissmueller "tobias@wissmueller.net"  
RUN gem install jekyll-gist therubyracer json --no-doc --no-ri  
ADD . /srv/jekyll  
CMD ["jekyll", "serve"]  

