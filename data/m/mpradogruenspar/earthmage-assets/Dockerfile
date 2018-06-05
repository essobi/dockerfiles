FROM phusion/passenger-customizable:0.9.20  
MAINTAINER Jan Papenbrock <j.papenbrock@gruenspar.de>  
  
# PHP 5.x  
RUN apt-get update && apt-get install -y php php-gd  
  
# RUBY 2.2  
RUN /pd_build/ruby-2.2.*.sh  
  
# nodejs  
RUN /pd_build/nodejs.sh  
  
# grunt cli  
RUN npm install -g grunt-cli  
  
# Install ruby gems  
WORKDIR /tmp  
ADD Gemfile Gemfile  
ADD Gemfile.lock Gemfile.lock  
RUN gem install bundler  
RUN bundle install  
  
# Install node modules required for compilation  
RUN mkdir /npm  
WORKDIR /npm  
ADD package.json package.json  
RUN npm install  
  
# Main worker script  
ADD compile /opt/compile  
  
# Compiling! https://xkcd.com/303/  
CMD ["compile", "all"]  
ENTRYPOINT ["/opt/compile"]  
  
# Clean up APT when done.  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

