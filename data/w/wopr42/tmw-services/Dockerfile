FROM ruby:2.4  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
libc6-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp \  
&& curl -O ftp://ftp.freetds.org/pub/freetds/stable/freetds-1.00.tar.bz2 \  
&& tar xf freetds-1.00.tar.bz2 \  
&& cd freetds-1.00 \  
&& ./configure --prefix=/usr/local \--with-tdsver=7.0 \  
&& make \  
&& make install  
  
WORKDIR /app  
COPY Gemfile* ./  
RUN bundle install --jobs 5 --retry 5  
COPY . .  
  
EXPOSE 3000  
CMD ['rails', 'server', '-b', '0.0.0.0']  

