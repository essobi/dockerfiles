FROM python:3.6  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y cmake \  
&& wget "https://github.com/google/brotli/archive/v1.0.1.tar.gz" -O
/tmp/brotli.tar.gz \  
&& tar xf /tmp/brotli.tar.gz -C /tmp \  
&& cd /tmp/brotli-1.0.1 \  
&& ./configure-cmake \  
&& make install \  
&& rm -rf /tmp/brotli.tar.gz /tmp/brotli-1.0.1 \  
&& apt-get autoremove -y cmake \  
  
&& wget
https://downloads.sourceforge.net/project/optipng/OptiPNG/optipng-0.7.6/optipng-0.7.6.tar.gz
-O /tmp/optipng.tar.gz \  
&& tar xf /tmp/optipng.tar.gz -C /tmp \  
&& cd /tmp/optipng-0.7.6 \  
&& ./configure \  
&& make install  
  
ADD . /data/app  
  
WORKDIR "/work"  
  
ENTRYPOINT ["/data/app/compress.py"]  

