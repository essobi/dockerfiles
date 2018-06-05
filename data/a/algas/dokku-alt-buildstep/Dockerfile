FROM progrium/cedarish:cedar14  
MAINTAINER Jeff Lindsay <progrium@gmail.com>  
  
ADD ./stack/configs/etc-profile /etc/profile  
  
ADD ./builder/ /build  
RUN xargs -L 1 /build/install-buildpack /tmp/buildpacks <
/build/config/buildpacks.txt  
  
RUN gem install foreman  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential uuid-dev libmysqlclient-dev git
libxml2-dev libxslt1-dev libzmq-dev librsvg2-dev libmagickcore-dev  
  
ENV APP_DIR /app  
  
RUN mkdir -p $APP_DIR/swfmill/bin  
ADD ./swfmill $APP_DIR/swfmill/bin/  
  
ADD http://download.zeromq.org/zeromq-2.2.0.tar.gz /tmp/zeromq-2.2.0.tar.gz  
RUN mkdir -p $APP_DIR/zeromq  
RUN cd /tmp && tar xzf zeromq-2.2.0.tar.gz && cd /tmp/zeromq-2.2.0 &&
./configure --prefix $APP_DIR/zeromq && make && make install && cd $APP_DIR  
  
ADD
https://launchpad.net/imagemagick/main/6.8.0-4/+download/ImageMagick-6.8.0-4.tar.gz
/tmp/ImageMagick-6.8.0-4.tar.gz  
RUN mkdir -p $APP_DIR/ImageMagick  
RUN cd /tmp && tar xzf ImageMagick-6.8.0-4.tar.gz && cd
/tmp/ImageMagick-6.8.0-4 && ./configure --prefix $APP_DIR/ImageMagick && make
&& make install && cd $APP_DIR  
  
ENV PORT 5000  
EXPOSE 5000  

