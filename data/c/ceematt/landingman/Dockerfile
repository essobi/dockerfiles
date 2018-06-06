FROM drydock/u14:prod  
MAINTAINER Matt Snider (matt@cleanenergyexperts.com)  
  
# Updating Apt-get  
RUN mkdir -p /tmp && chmod 1777 /tmp  
RUN apt-add-repository -y ppa:brightbox/ruby-ng  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN add-apt-repository -y ppa:danmbox/ppa  
RUN apt-get -y update  
  
# Install Ruby 2.2  
RUN apt-get -y install ruby2.2 ruby2.2-dev  
RUN gem install bundler  
  
# Install NodeJS  
RUN apt-get -y install nodejs  
RUN npm install -g svgo  
  
# Install Dependencies  
RUN apt-get -y install \  
libpng-dev \  
libxml2 \  
libxml2-dev \  
libxslt1-dev \  
libssl-dev \  
g++ \  
zlib1g-dev \  
checkinstall \  
zip  
  
# Install Image Libraries: optipng, pngcrush  
RUN apt-get -y install advancecomp gifsicle jhead jpegoptim libjpeg-progs
optipng pngcrush pngquant  
  
# Install PNGOUT  
RUN wget http://static.jonof.id.au/dl/kenutils/pngout-20130221-linux.tar.gz &&
\  
tar xvzf pngout-20130221-linux.tar.gz && \  
rm pngout-20130221-linux.tar.gz && \  
mv pngout-20130221-linux/x86_64/pngout /usr/local/bin/ && \  
rm -rf pngout-20130221-linux  
  
# Install Imagemagick  
RUN apt-get build-dep -y imagemagick  
RUN apt-get install -y libmagickwand-dev libmagickcore-dev libmagickcore-extra
libgraphviz-dev  
RUN wget http://www.imagemagick.org/download/ImageMagick.tar.gz && \  
mkdir ImageMagick && \  
tar -xzvf ImageMagick.tar.gz -C ImageMagick --strip-components=1 && \  
rm ImageMagick.tar.gz && \  
cd ImageMagick && \  
./configure && \  
make && \  
make install && \  
ldconfig /usr/local/lib  
  
# Install PhantomJS 1.9.8  
RUN apt-get -y install libicu-dev libfontconfig fontconfig  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2
&& \  
tar -vxjf phantomjs-1.9.8-linux-x86_64.tar.bz2 && \  
rm phantomjs-1.9.8-linux-x86_64.tar.bz2 && \  
mv phantomjs-1.9.8-linux-x86_64/bin/phantomjs /usr/local/bin/ && \  
rm -rf phantomjs-1.9.8-linux-x86_64  
  
# Install qt & xvfb  
RUN apt-get -y install libqtwebkit-dev gstreamer1.0-plugins-base
gstreamer1.0-tools gstreamer1.0-x  
RUN apt-get -y install xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic

