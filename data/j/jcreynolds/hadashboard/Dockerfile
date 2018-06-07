FROM ruby:2.2.5  
MAINTAINER jcreynolds  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update \  
&& apt-get install -y \  
sqlite \  
nodejs \  
libpq-dev \  
libssl-dev \  
libsqlite3-dev \  
ruby-dev \  
python3 \  
python3-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY . .  
  
VOLUME /usr/src/app/lib /usr/src/app/dashboards /usr/src/app/hapush
/usr/src/app/widgets  
  
EXPOSE 3030  
RUN gem install dashing \  
&& gem install bundler \  
&& bundle \  
&& pip3 install daemonize sseclient configobj \  
&& pip3 install --upgrade requests  
  
CMD /usr/src/app/hapush/hapush.py -d /hapush/hapush.cfg && dashing start  

