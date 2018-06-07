FROM ruby:1.9.3  
  
MAINTAINER Tomasz Niec <errno@errno.info>  
RUN apt-get update && \  
apt-get -y install nodejs && \  
apt-get -y clean  
RUN gem install bundler dashing  
RUN mkdir /dashing && \  
dashing new dashing && \  
cd /dashing && \  
bundle && \  
ln -s /dashing/dashboards /dashboards && \  
ln -s /dashing/jobs /jobs && \  
ln -s /dashing/assets /assets && \  
ln -s /dashing/lib /lib-dashing && \  
ln -s /dashing/public /public && \  
ln -s /dashing/widgets /widgets && \  
ln -s /dashing/images /images && \  
mkdir /dashing/config && \  
mv /dashing/config.ru /dashing/config/config.ru && \  
ln -s /dashing/config/config.ru /dashing/config.ru && \  
ln -s /dashing/config /config && \  
ln -s /dashing/config/bitbucket.rb /dashing/bitbucket.rb && \  
ln -s /dashing/config/jenkins.rb /dashing/jenkins.rb && \  
ln -s /dashing/config/dashing.iml /dashing/dashing.iml  
  
COPY run.sh /  
  
VOLUME ["/dashboards", "/jobs", "/lib-dashing", "/config", "/public",
"/widgets", "/assets", "/images"]  
  
ENV PORT 3030  
EXPOSE $PORT  
WORKDIR /dashing  
  
CMD ["/run.sh"]  
  

