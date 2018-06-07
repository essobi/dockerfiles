FROM buildpack-deps:jessie  
MAINTAINER Joerg Patzer <joerg.patzer@me.com>  
  
# Warning: Compiling PhantomJS from source takes a long time, mainly due to
thousands of files in the WebKit module.  
  
ENV PHANTOM_VERSION 2.0.0  
  
COPY ./infinality /tmp  
  
RUN sed -i "s/jessie main/jessie main contrib/" /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \  
build-essential \  
g++ \  
flex \  
bison \  
gperf \  
ruby \  
perl \  
libsqlite3-dev \  
libfontconfig1-dev \  
libicu-dev \  
libfreetype6 \  
libssl-dev \  
libpng-dev \  
libjpeg-dev \  
python \  
libx11-dev \  
libxext-dev \  
ttf-mscorefonts-installer \  
&& curl -L
https://github.com/ariya/phantomjs/archive/${PHANTOM_VERSION}.tar.gz | tar
-xzC /tmp \  
&& cd /tmp/phantomjs-${PHANTOM_VERSION} \  
&& ./build.sh --confirm --silent --jobs 2 \  
&& mv bin/phantomjs /usr/local/bin \  
&& cd /tmp \  
&& dpkg -i *-infinality*.deb \  
&& printf "4\n" | /etc/fonts/infinality/infctl.sh setstyle \  
&& apt-get purge --auto-remove -y \  
build-essential \  
curl \  
g++ \  
flex \  
bison \  
gperf \  
ruby \  
perl \  
python \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/*  
  
WORKDIR /tmp  
  
# expose port for webdriver option  
EXPOSE 8910  
  
# make container as a executable, e.g. docker run --rm <image> 'phantomjs
argument'  
ENTRYPOINT ["/usr/local/bin/phantomjs"]  

