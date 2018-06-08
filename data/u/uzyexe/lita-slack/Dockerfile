FROM litaio/ruby:2.2.2  
ENV LITA_VERSION 4.3.2  
ENV LITA_INFO_LEVEL debug  
ENV SLACK_TOKEN YOUR_SLACK_TOKEN  
ENV REDIS_HOST 127.0.0.1  
ENV REDIS_PORT 6379  
RUN mkdir /opt/lita  
  
WORKDIR /opt/lita  
VOLUME /opt/lita  
  
ADD setup.sh setup.sh  
  
RUN echo "gem: --no-ri --no-rdoc" > /.gemrc && \  
gem install lita -v ${LITA_VERSION} && \  
gem install lita-slack  
  
CMD if [ -e ./setup.sh ]; then \  
./setup.sh; \  
fi && \  
bundle install && \  
lita start  

