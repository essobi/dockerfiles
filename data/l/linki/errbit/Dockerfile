FROM ubuntu:15.04  
MAINTAINER Linki <linki+docker.com@posteo.de>  
  
# update the package list  
RUN apt-get update  
  
# install build-essential because we need to compile some native extensions  
RUN apt-get install -y build-essential  
  
# install zlib development headers for nokogiri to build  
#  
# http://www.nokogiri.org/tutorials/installing_nokogiri.html  
#  
RUN apt-get install -y zlib1g-dev  
  
# we need a javascript runtime  
RUN apt-get -y install nodejs  
  
# install git in order to checkout the project and gems defined by git urls  
RUN apt-get -y install git-core  
  
# install ruby 2.1 with development extensions  
RUN apt-get install -y ruby2.1 ruby2.1-dev  
  
# install our beloved bundler  
RUN gem install bundler  
  
# clone errbit's default branch  
RUN git clone \--depth 1 https://github.com/errbit/errbit.git /app  
  
# add some gems specific to this image build  
COPY ./files/UserGemfile /app/UserGemfile  
  
# create an unprivileged user that owns the code and will run the app server  
RUN useradd -m app  
RUN chown -R app:app /app  
  
# switch to the app user from now on  
USER app  
  
# set the working directory to the app  
WORKDIR /app  
  
# install all ruby dependencies via bundler into a local path  
RUN bundle install --path ./vendor/bundle  
  
# precompile all assets  
RUN bundle exec rake assets:precompile  
  
# expose the app server's port  
EXPOSE 3000  
# launch the rails server unless another command is given  
CMD bundle exec rails s thin -p 3000 -b 0.0.0.0  

