FROM ruby:latest  
  
ENV JQ_VERSION=1.5  
RUN \  
cd /tmp && \  
git clone \--branch jq-$JQ_VERSION https://github.com/stedolan/jq.git && \  
cd jq && \  
autoreconf -i && \  
./configure --enable-shared --disable-maintainer-mode && \  
make && \  
make install && \  
ldconfig  
  
RUN gem install ruby-jq  

