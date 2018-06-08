FROM openjdk:8  
MAINTAINER Sathwik B P  
  
ENV JRUBY_VERSION 9.1.12.0  
ENV BUILDR_VERSION 1.5.3  
ENV JRUBY_OPENSSL_VERSION 0.9.17  
ENV RSPEC-EXPECTATIONS 2.14.3  
ENV RSPEC-MOCKS 2.14.3  
ENV RSPEC-CORE 2.14.5  
ENV RSPEC 2.14.1  
ENV NOKOGIRI 1.6.8  
RUN mkdir /opt/jruby \  
&& curl http://jruby.org.s3.amazonaws.com/downloads/${JRUBY_VERSION}/jruby-
bin-${JRUBY_VERSION}.tar.gz \  
| tar -zxC /opt/jruby --strip-components=1 \  
&& update-alternatives --install /usr/local/bin/ruby ruby /opt/jruby/bin/jruby
1  
  
ENV PATH /opt/jruby/bin:$PATH  
  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
  
RUN gem install bundler  
RUN gem install jruby-openssl -v ${JRUBY_OPENSSL_VERSION}  
RUN gem install buildr -v ${BUILDR_VERSION}  
RUN gem install rspec-expectations -v ${RSPEC-EXPECTATIONS}  
RUN gem install rspec-mocks -v ${RSPEC-MOCKS}  
RUN gem install rspec-core -v ${RSPEC-CORE}  
RUN gem install rspec -v ${RSPEC}  
RUN gem install nokogiri -v ${NOKOGIRI}  
  
# make /tmp available to all users.  
RUN chmod 777 -R /tmp && chmod o+t -R /tmp  
  
RUN update-alternatives --install /usr/local/bin/buildr buildr
/opt/jruby/bin/buildr 1 \  
&& update-alternatives --install /usr/local/bin/jruby jruby
/opt/jruby/bin/jruby 1  
  
ENV WORKSPACE /workspace  
VOLUME /workspace  
WORKDIR /workspace  
  
ENTRYPOINT [ "buildr" ]  

