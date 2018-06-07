FROM frvi/ruby  
  
MAINTAINER Fredrik Vihlborg <fredrik.wihlborg@gmail.com>  
  
RUN apt-get update -y && apt-get install -y git  
RUN gem install bundle  
COPY Gemfile /  
RUN bundle  
RUN mkdir /dashing && \  
bundle exec dashing new dashing && \  
cd /dashing && \  
bundle && \  
ln -s /dashing/dashboards /dashboards && \  
ln -s /dashing/jobs /jobs && \  
ln -s /dashing/assets /assets && \  
ln -s /dashing/lib /lib-dashing && \  
ln -s /dashing/public /public && \  
ln -s /dashing/widgets /widgets && \  
mkdir /dashing/config && \  
mv /dashing/config.ru /dashing/config/config.ru && \  
ln -s /dashing/config/config.ru /dashing/config.ru && \  
ln -s /dashing/config /config  
  
COPY run.sh /  
  
VOLUME ["/dashboards", "/jobs", "/lib-dashing", "/config", "/public",
"/widgets", "/assets"]  
  
ENV PORT 3030  
EXPOSE $PORT  
WORKDIR /dashing  
  
CMD ["/run.sh"]  
  

