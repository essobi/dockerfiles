FROM ruby:2.2.4  
MAINTAINER Kevin Traver (Greenstone Homes)  
  
RUN apt-get update && apt-get install -y curl --no-install-recommends  
RUN apt-get update && apt-get install -y nodejs --no-install-recommends  
RUN apt-get update && apt-get install -y sqlite --no-install-recommends  
RUN apt-get update && apt-get install -y qt5-default --no-install-recommends  
RUN apt-get update && apt-get install -y libgtk2.0-dev --no-install-recommends  
RUN apt-get update && apt-get install -y libqt5webkit5-dev --no-install-
recommends  
RUN apt-get update && apt-get install -y cron --no-install-recommends  
RUN apt-get update && apt-get install -y rsyslog --no-install-recommends  
RUN apt-get update && apt-get install -y libfontconfig1 --no-install-
recommends  
RUN apt-get update && apt-get install -y build-essential --no-install-
recommends  
RUN apt-get update && apt-get install -y libc6-dev --no-install-recommends  
  
WORKDIR /tmp  
RUN wget ftp://ftp.freetds.org/pub/freetds/stable/freetds-1.00.80.tar.gz  
RUN tar -xzf freetds-1.00.80.tar.gz  
WORKDIR /tmp/freetds-1.00.80  
RUN ./configure --prefix=/usr/local \--with-tdsver=7.3  
RUN make  
RUN make install  
  
WORKDIR /tmp  
RUN wget -q
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
RUN tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN cp wkhtmltox/bin/wkhtmltopdf /usr/bin/wkhtmltopdf  
  
WORKDIR /tmp  
RUN wget -q
https://cnpmjs.org/mirrors/phantomjs/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin  
  
RUN gem install bundler --no-ri --no-rdoc  
  
WORKDIR /  
  
ADD Gemfile Gemfile  
  
RUN bundle install  
  
RUN rm Gemfile  
  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/*  
  
CMD ["bundle install"]  

