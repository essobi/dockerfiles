FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
locales \  
nodejs \  
nodejs-legacy \  
nodejs-dev \  
npm \  
ruby \  
ruby-dev \  
&& gem install listen sass compass scss-lint \  
&& npm install -g npm@latest \  
&& npm install -g grunt-cli  
  
WORKDIR /srv  
VOLUME /srv  
  
ENV LC_ALL=C.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["grunt"]  

