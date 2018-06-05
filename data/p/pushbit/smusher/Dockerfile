FROM pushbit/ruby  
  
MAINTAINER Tom Moor "tom.moor@gmail.com"  
RUN apt-get update  
  
# mozjpeg  
RUN apt-get install -y autoconf automake libtool nasm make  
RUN mkdir mozjpeg  
RUN wget -O - https://github.com/mozilla/mozjpeg/archive/v1.0.1.tar.gz | tar
xzf - --strip-components=1 -C "/mozjpeg"  
RUN ls -la  
WORKDIR /mozjpeg  
RUN autoreconf -fiv  
RUN mkdir build  
WORKDIR /mozjpeg/build  
RUN sh ../configure  
RUN make install  
RUN ln -s /opt/libmozjpeg/bin/jpegtran /usr/local/bin/mozjpeg  
WORKDIR /  
  
# pngquant  
RUN apt-get install -y pngquant  
  
RUN gem install faraday  
  
ADD ./execute.rb ./execute.rb  
  
CMD ["ruby", "./execute.rb"]

