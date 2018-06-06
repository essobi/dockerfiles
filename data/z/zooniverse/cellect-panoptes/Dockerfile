FROM zooniverse/ruby:2.3  
WORKDIR /cellect_panoptes  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && \  
apt-get install -y --no-install-recommends autoconf automake \  
libboost-all-dev libffi-dev git-core supervisor libpq-dev && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ./Gemfile /cellect_panoptes/  
ADD ./Gemfile.lock /cellect_panoptes/  
  
RUN bundle install --without development test  
  
ADD supervisord.conf /etc/supervisor/conf.d/cellect.conf  
ADD ./ /cellect_panoptes  
  
RUN chmod +x /cellect_panoptes/cellect_start  
  
EXPOSE 80  
ENTRYPOINT [ "/usr/bin/supervisord" ]  

