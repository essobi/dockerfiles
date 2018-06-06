FROM ruby:2.2  
MAINTAINER Ingolf Wagner <docker@ingolf-wagner.de>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
sqlite3 \  
libsqlite3-dev \  
&& gem install mailcatcher \  
-v 0.6.5 \--no-ri --no-rdoc \  
&& apt-get remove --purge -y \  
build-essential \  
libsqlite3-dev \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# smtp port  
EXPOSE 1025  
# webserver port  
EXPOSE 1080  
  
RUN useradd mailcatcher  
USER mailcatcher  
  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]  

