FROM ruby:2.3.4-slim  
  
# RUN apk update && apk add make git nodejs gcc build-base sqlite-dev python  
RUN apt-get update && apt-get install --no-install-recommends -y git nodejs
make gcc g++ libsqlite3-dev locales  
  
RUN locale-gen en_US.UTF-8 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure
locales  
RUN echo "LANG=C.UTF-8\nLC_ALL=C.UTF-8\nLC_CTYPE=C.UTF-8" >> /etc/environment  
  
# RUN gem install bundler && gem install rubygems-bundler && gem
regenerate_binstubs  
RUN gem install bundler  
  
# RUN gem install therubyracer -- --use-system-libraries  
RUN mkdir -p /opt && cd /opt && git clone \--depth 1
git://github.com/beefproject/beef.git  
RUN cd /opt/beef && bundle install  
  
EXPOSE 2000 3000  
# update-locale LANG=en_US.UTF-8  
# RUN echo "export LANG=en_US.UTF-8\nexport LANGUAGE=en_US.UTF-8\nexport
LC_ALL=en_US.UTF-8" >> ~/.profile  
#ENTRYPOINT ["/usr/local/bin/ruby","-C","/opt/beef","/opt/beef/beef"]  
CMD LC_ALL="C.UTF-8" /usr/local/bin/ruby -C /opt/beef /opt/beef/beef  

