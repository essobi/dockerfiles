FROM ruby:2.3  
MAINTAINER T Chusri <t.chusri@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -yq software-properties-common  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -yq build-essential libssl-dev libyaml-dev git libtool
libxslt-dev libxml2-dev libpq-dev gawk curl pngcrush python-software-
properties libcurl4-openssl-dev parallel patch ruby-dev zlib1g-dev liblzma-dev
libgmp-dev cron psmisc rsyslog vim whois advancecomp jhead jpegoptim libjpeg-
turbo-progs optipng make automake m4 gcc libc-dev  
  
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -yq nodejs  
RUN npm install uglify-js -g  
RUN npm install svgo -g  
RUN bundle config build.nokogiri --use-system-libraries  
  
# consider upgrading this  
RUN mkdir /jemalloc && cd /jemalloc &&\  
wget http://www.canonware.com/download/jemalloc/jemalloc-3.6.0.tar.bz2 &&\  
tar -xjf jemalloc-3.6.0.tar.bz2 && cd jemalloc-3.6.0 && ./configure && make
&&\  
mv lib/libjemalloc.so.1 /usr/lib && cd / && rm -rf /jemalloc  
  
RUN echo 'gem: --no-document' >> /usr/local/etc/gemrc &&\  
mkdir /src && cd /src && git clone https://github.com/sstephenson/ruby-
build.git &&\  
cd /src/ruby-build && ./install.sh &&\  
cd / && rm -rf /src/ruby-build && ruby-build 2.3.1 /usr/local  
  
RUN gem install bundler &&\  
rm -rf /usr/local/share/ri/2.3.0/system &&\  
cd / && git clone https://github.com/SamSaffron/pups.git  
  
ADD install-imagemagick /tmp/install-imagemagick  
RUN /tmp/install-imagemagick  
  
RUN ruby -e "v='`convert -version`'; ['png','tiff','jpeg','freetype'].each{
|f| ((STDERR.puts('no ' + f + ' support in imagemagick')); exit(-1)) unless
v.include?(f)}"  
  
ADD install-pngcrush /tmp/install-pngcrush  
RUN /tmp/install-pngcrush  
  
ADD install-gifsicle /tmp/install-gifsicle  
RUN /tmp/install-gifsicle  
  
ADD install-pngquant /tmp/install-pngquant  
RUN /tmp/install-pngquant  
  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  

