FROM ubuntu:14.04  
MAINTAINER The Doalitic team  
  
ADD . /tmp  
WORKDIR /tmp/blog  
RUN rm -rf public/*  
RUN mkdir -p /var/www/blog  
RUN chown www-data:www-data /var/www/blog  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y dist-upgrade && \  
apt-get -y install python-pip wget && rm -rf /var/lib/apt/lists/*  
RUN wget
https://github.com/spf13/hugo/releases/download/v0.16/hugo_0.16-1_amd64.deb &&
\  
dpkg -i hugo_0.16-1_amd64.deb  
RUN pip install Pygments  
  
USER www-data  
CMD [ "hugo", "-d", "/var/www/blog/" ]  

