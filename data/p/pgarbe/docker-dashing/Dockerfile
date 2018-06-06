FROM ruby:1.9  
  
RUN apt-get update  
RUN apt-get -y install npm  
RUN apt-get -y install nodejs  
  
RUN gem install dashing  
RUN gem install bundle  
  
RUN mkdir /dashing && \  
dashing new dashing && \  
cd /dashing && bundle && \  
ln -s /dashing/dashboards /dashboards && \  
ln -s /dashing/jobs /jobs && \  
ln -s /dashing/public /public && \  
ln -s /dashing/widgets /widgets && \  
mkdir /dashing/config && \  
mv /dashing/config.ru /dashing/config/config.ru && \  
ln -s /dashing/config/config.ru /dashing/config.ru && \  
ln -s /dashing/config /config  
  
# COPY run.sh /  
  
VOLUME ["/dashboards", "/jobs", "/config", "/public", "/widgets"]  
  
# Run Bundle in a cache efficient way  
WORKDIR /tmp  
ADD Gemfile /tmp/  
ADD Gemfile.lock /tmp/  
RUN bundle install  
  
ENV PORT 3030  
EXPOSE $PORT  
WORKDIR /dashing  
  
# CMD ["/run.sh"]  
# CMD ["/bin/bash"]  
CMD ["dashing start $PORT"]  

