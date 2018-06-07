FROM trenpixster/elixir  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -s
https://raw.githubusercontent.com/wayneeseguin/rvm/master/binscripts/rvm-
installer | bash -s stable --ruby  
  
ENV RUBY_VERSION 2.2.1  
ENV PATH
/usr/local/rvm/gems/ruby-$RUBY_VERSION/bin:/usr/local/rvm/gems/ruby-$RUBY_VERSION@global/bin:/usr/local/rvm/rubies/ruby-$RUBY_VERSION/bin:$PATH:/usr/local/rvm/bin  
  
RUN gem install ernie  
RUN mkdir -p /data/logs  
ADD ernie.config /data/ernie.config  
ADD examples/ /data/examples/  
  
WORKDIR /data  
VOLUME /data  
EXPOSE 9999  
CMD ["ernie", "-c", "/data/ernie.config", "-p", "9999", "-a",
"/data/logs/access.log"]  

