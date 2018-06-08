FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV RACK_ENV production  
  
RUN apt-get update && apt-get install -y git bundler libmysqlclient-dev  
RUN git clone https://github.com/posty/posty_api.git /srv/posty_api  
  
RUN cd /srv/posty_api && bundle install  
  
ADD files/entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
RUN useradd -m posty && chown -R posty:posty /srv/posty_api  
USER posty  
EXPOSE 9292  
WORKDIR /srv/posty_api  
ENTRYPOINT /entrypoint.sh  

