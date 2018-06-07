FROM ruby:2.2  
COPY Gemfile /Gemfile  
RUN bundle install  
  
RUN useradd -u 1000 -M docker \  
&& mkdir -p /messages/sns \  
&& chown docker /messages/sns  
USER docker  
  
VOLUME /messages/sns  
EXPOSE 9292  
# Note: We use thin, because webrick attempts to do a reverse dns lookup on
every request  
# which slows the service down big time. There is a setting to override this,
but sinatra  
# does not allow server specific settings to be passed down.  
CMD fake_sns --bind 0.0.0.0 --database=/messages/sns/database.yml --port 9292
--server thin  

