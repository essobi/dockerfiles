FROM ruby:2.4.2-jessie  
MAINTAINER Aaron Florey <devs@elliscreative.com.au>  
  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# for node  
RUN apt-get install -y python python-dev python-pip python-virtualenv  
  
# install node repo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# install nodejs  
RUN apt-get install -y nodejs  
  
# install yarn repo  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# install yarn  
RUN apt-get update && apt-get install yarn  
  
# install sass gem  
RUN gem install sass  
  
WORKDIR /app  
ONBUILD ADD . /app  
  
CMD ["bash"]  

