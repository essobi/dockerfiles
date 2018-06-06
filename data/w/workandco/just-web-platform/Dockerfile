FROM rails:4.2.6  
MAINTAINER Eric Olivas <olivas@work.co>  
  
# Basic linux dependencies  
RUN apt-get -y update &&\  
apt-get install -y \  
imagemagick \  
cron \  
curl \  
netcat \  
libqtwebkit-dev \  
redis-tools \  
gstreamer1.0-plugins-base \  
gstreamer1.0-tools \  
gstreamer1.0-x  
  
RUN mkdir -p /workdir/app  
RUN mkdir -p /workdir/tmp  
RUN chmod 775 -R /workdir  
  
VOLUME /workdir  
WORKDIR /workdir  
  
COPY Gemfile /tmp  
COPY Gemfile.lock /tmp  
RUN gem install bundler  
RUN cd /tmp && bundle install  
EXPOSE 3000  
COPY ./docker/scripts/ /tmp  
RUN cd /tmp && chmod 755 -R /tmp/ && ls -ltra  
  
ENV HOST_TO_WAIT_FOR "just-postgres 5432"  
CMD /tmp/start.sh && /tmp/run.sh

