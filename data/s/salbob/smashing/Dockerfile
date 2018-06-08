FROM ruby:2.3.1  
MAINTAINER Eric Bussieres <erbussieres@gmail.com>  
  
RUN apt-get update && \  
apt-get -y install nodejs && \  
apt-get -y clean  
RUN gem install bundler smashing httparty json  
  
RUN smashing new smashing && \  
cd /smashing && \  
bundle  
  
RUN rm -rf /smashing/widgets/* && \  
rm -rf /smashing/dashboards/* && \  
rm -rf /smashing/jobs/* && \  
rm -rf /smashing/Gemfile  
  
COPY run.sh /smashing/  
COPY Gemfile /smashing/  
RUN chmod 775 /smashing/run.sh  
  
ENV PORT 3030  
EXPOSE $PORT  
WORKDIR /smashing  
  
CMD ["/smashing/run.sh"]

