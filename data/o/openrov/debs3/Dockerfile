FROM debian:wheezy  
MAINTAINER OpenROV Inc - Dominik Fretz, dominik@openrov.com  
ENV HOME /root  
  
RUN apt-get update && apt-get install -y \  
ruby1.9.3 \  
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
RUN git clone https://github.com/BrianAdams/deb-s3.git  
  
WORKDIR /tmp/deb-s3  
RUN git checkout 26bf2096207af0bf2779556dd03af70197850fa7 && bundle install  
  
ENTRYPOINT ["/tmp/deb-s3/bin/deb-s3"]  
CMD ["help"]  

