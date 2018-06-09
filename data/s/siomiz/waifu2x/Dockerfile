FROM ubuntu:14.04  
  
MAINTAINER Tomohisa Kusano <siomiz@gmail.com>  
  
ENV OPENCV_VERSION 3.0.0  
ENV W2XCONV_VERSION v1.1.1  
  
COPY *.sh /  
  
RUN mkdir -p /opt/w2x \  
&& bash /build.sh \  
&& rm /build.sh \  
&& useradd --no-create-home --home-dir / user \  
&& chmod +x /entrypoint.sh \  
&& chown -R user /opt/w2x  
  
WORKDIR /opt/w2x  
  
USER user  
  
ENTRYPOINT ["/entrypoint.sh"]  

