FROM ruby:2.3.0  
ENV PORT 3030  
  
# install node and build tools  
RUN apt-get update -qq && apt-get install -y build-essential nodejs npm  
RUN apt-get -y clean  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# install dashing.io  
RUN gem install puma  
RUN gem install dashing  
RUN gem install bundle  
  
# set up dashing  
RUN cd /usr/src && \  
dashing new dashing && \  
cd /usr/src/dashing  
  
# copy the working dashing directories  
COPY . /usr/src/dashing  
  
# set up the linked dashing directories just incase you want any overrides  
RUN ln -s /usr/src/dashing/dashboards /dashboards && \  
ln -s /usr/src/dashing/jobs /jobs && \  
ln -s /usr/src/dashing/public /public && \  
ln -s /usr/src/dashing/widgets /widgets && \  
mkdir /usr/src/dashing/config && \  
mv /usr/src/dashing/config.ru /usr/src/dashing/config/config.ru && \  
ln -s /usr/src/dashing/config/config.ru /usr/src/dashing/config.ru && \  
ln -s /usr/src/dashing/config /config  
  
#install any missing gems for the widgets and compile the widgets  
# Run Bundle in a cache efficient way  
WORKDIR /tmp  
ADD Gemfile /tmp/  
ADD Gemfile.lock /tmp/  
RUN bundle install  
  
VOLUME ["/usr/src/dashing", "/config", "/dashboards", "/jobs", "/public",
"/widgets"]  
  
WORKDIR /usr/src/dashing  
  
EXPOSE $PORT  
CMD ["puma", "-p", "3030", "config.ru"]  

