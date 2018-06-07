FROM debian:stretch  
ENV HOME /root  
  
RUN apt-get update && apt-get install -y \  
ruby \  
rubygems \  
gnupg \  
gnupg-agent \  
dpkg-sig \  
git \  
libxml2 \  
libxml2-dev \  
libxslt-dev  
  
RUN gem install bundler  
  
WORKDIR /tmp  
RUN git clone https://github.com/krobertson/deb-s3.git  
  
WORKDIR /tmp/deb-s3  
RUN bundle install  
  
ENTRYPOINT ["/tmp/deb-s3/bin/deb-s3"]  
CMD ["help"]  

