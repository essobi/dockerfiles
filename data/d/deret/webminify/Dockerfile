FROM openjdk:8-jre  
  
# https://github.com/google/closure-compiler/wiki/Binary-Downloads  
# https://github.com/google/closure-stylesheets/releases  
# https://github.com/google/guetzli/releases  
# https://github.com/mozilla/mozjpeg/releases  
# https://pngquant.org/releases.html  
# https://johnvansickle.com/ffmpeg/  
  
ENV CLOSURECOMPILER_VERSION 20171112  
ENV CLOSURESTYLESHEETS_VERSION 1.5.0  
ENV GUETZLI_VERSION 1.0.1  
ENV MOZJPEG_VERSION 3.2  
ENV PNGQUANT_VERSION 2.11.2  
  
RUN apt-get update \  
&& apt-get install -y build-essential imagemagick libpng-dev nasm php  
  
# closure compiler  
RUN mkdir /var/opt/closurecompiler-${CLOSURECOMPILER_VERSION} \  
&& cd /var/opt/closurecompiler-${CLOSURECOMPILER_VERSION} \  
&& wget http://dl.google.com/closure-
compiler/compiler-${CLOSURECOMPILER_VERSION}.tar.gz \  
&& tar -xzf compiler-${CLOSURECOMPILER_VERSION}.tar.gz \  
&& rm compiler-${CLOSURECOMPILER_VERSION}.tar.gz \  
&& echo "java -jar
/var/opt/closurecompiler-${CLOSURECOMPILER_VERSION}/closure-
compiler-v${CLOSURECOMPILER_VERSION}.jar \$*" > /usr/bin/closure-compiler \  
&& chmod +x /usr/bin/closure-compiler  
  
# closure stylesheets  
RUN mkdir /var/opt/closurestylesheets-${CLOSURESTYLESHEETS_VERSION} \  
&& cd /var/opt/closurestylesheets-${CLOSURESTYLESHEETS_VERSION} \  
&& wget https://github.com/google/closure-
stylesheets/releases/download/v${CLOSURESTYLESHEETS_VERSION}/closure-
stylesheets.jar \  
&& echo "java -jar
/var/opt/closurestylesheets-${CLOSURESTYLESHEETS_VERSION}/closure-
stylesheets.jar \$*" > /usr/bin/closure-stylesheets \  
&& chmod +x /usr/bin/closure-stylesheets  
  
# guetzli  
RUN mkdir /var/opt/guetzli-${GUETZLI_VERSION} \  
&& cd /var/opt/guetzli-${GUETZLI_VERSION} \  
&& wget
https://github.com/google/guetzli/releases/download/v${GUETZLI_VERSION}/guetzli_linux_x86-64
\  
&& ln -s /var/opt/guetzli-${GUETZLI_VERSION}/guetzli_linux_x86-64
/usr/bin/guetzli \  
&& chmod +x /usr/bin/guetzli  
  
# mozjpeg  
RUN cd /var/opt \  
&& wget
https://github.com/mozilla/mozjpeg/releases/download/v${MOZJPEG_VERSION}/mozjpeg-${MOZJPEG_VERSION}-release-
source.tar.gz \  
&& tar -xzf mozjpeg-${MOZJPEG_VERSION}-release-source.tar.gz \  
&& rm mozjpeg-${MOZJPEG_VERSION}-release-source.tar.gz \  
&& cd mozjpeg \  
&& ./configure \  
&& make \  
&& make install \  
&& ln -s /var/opt/mozjpeg/cjpeg /usr/bin/cjpeg \  
&& ln -s /var/opt/mozjpeg/djpeg /usr/bin/djpeg  
  
# pngquant  
RUN cd /var/opt \  
&& wget http://pngquant.org/pngquant-${PNGQUANT_VERSION}-src.tar.gz \  
&& tar -xzf pngquant-${PNGQUANT_VERSION}-src.tar.gz \  
&& rm pngquant-${PNGQUANT_VERSION}-src.tar.gz \  
&& cd pngquant-${PNGQUANT_VERSION} \  
&& make \  
&& make install  
  
# ffmpeg  
RUN cd /var/opt \  
&& wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz \  
&& tar --xz -xvf ffmpeg-release-64bit-static.tar.xz \  
&& rm ffmpeg-release-64bit-static.tar.xz \  
&& mv ffmpeg-* ffmpeg \  
&& ln -s /var/opt/ffmpeg/ffmpeg /usr/bin/ffmpeg \  
&& ln -s /var/opt/ffmpeg/ffmpeg-10bit /usr/bin/ffmpeg-10bit \  
&& ln -s /var/opt/ffmpeg/ffprobe /usr/bin/ffprobe \  
&& ln -s /var/opt/ffmpeg/ffserver /usr/bin/ffserver  
  
ENTRYPOINT /bin/bash  

