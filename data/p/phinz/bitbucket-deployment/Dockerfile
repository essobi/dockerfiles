FROM ruby:2.4  
MAINTAINER Pascal Hinz  
  
# @see https://rubygems.org/gems/compass  
# @see https://rubygems.org/gems/compass-core  
ENV COMPASS_VERSION 1.0.3  
# RUN gem install listen  
RUN gem install compass-core -v ${COMPASS_VERSION}  
RUN gem install compass -v ${COMPASS_VERSION}  
  
# copy deployment script  
COPY deploy.bash /  
RUN chmod a+x /deploy.bash  
  
# install ssh+rsync  
RUN apt-get update && apt-get -y install ssh rsync  
RUN mkdir -p ~root/.ssh && chmod 700 ~root/.ssh/  
  
VOLUME /src  
  
WORKDIR /src  
  
# cleanup  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT [ "compass" ]

