FROM inventid/base  
MAINTAINER inventid <tech@inventid.nl>  
  
EXPOSE 3000  
RUN mkdir /opt/stoplight-admin  
  
ADD Gemfile /opt/stoplight-admin/  
RUN bash -c "cd /opt/stoplight-admin && \  
source /usr/local/rvm/scripts/rvm && \  
rvm 2.2.3 && \  
bundle install"  
  
ADD app.rb /opt/stoplight-admin/  
WORKDIR /opt/stoplight-admin  
CMD bash -c "source /usr/local/rvm/scripts/rvm && \  
rvm use 2.2.3 && \  
bundle exec ruby app.rb"  
  

