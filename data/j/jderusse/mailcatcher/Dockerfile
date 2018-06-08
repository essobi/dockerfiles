FROM debian:latest  
MAINTAINER Jérémy Derussé "jeremy@derusse.com"  
# Install requirements  
RUN \  
apt-get update -qq && \  
apt-get install --no-install-recommends -y ruby sqlite3 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install build tools, then install mailcatcher, then remove build tools  
RUN \  
apt-get update -qq && \  
apt-get install --no-install-recommends -y build-essential ruby-dev
libsqlite3-dev && \  
  
gem install mailcatcher --no-ri --no-rdoc && \  
  
apt-get remove --purge -y build-essential ruby-dev libsqlite3-dev && \  
apt-get autoclean && apt-get clean && \  
  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  
EXPOSE 25  
  
CMD ["--smtp-port", "25", "--http-port", "80", "--ip", "0.0.0.0", "-f"]  
ENTRYPOINT ["mailcatcher"]  

