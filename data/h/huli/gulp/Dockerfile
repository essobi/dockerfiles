FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
curl \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash /dev/stdin \  
&& apt-get install -y nodejs  
  
RUN apt-get install -y \  
build-essential \  
ruby-full \  
rubygems \  
&& npm install -g gulp-cli \  
&& gem install sass compass  
  
WORKDIR /srv  
VOLUME /srv  
  
ENV LC_ALL=C.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["gulp"]  

