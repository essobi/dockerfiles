FROM ruby:2.4.1  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update -qq && \  
apt-get install -y \  
build-essential \  
libpq-dev \  
nodejs \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
#RUN cd /tmp/ && \  
# git clone https://github.com/OWASP/railsgoat goat && \  
# mkdir /myapp && \  
# cp /tmp/goat/Gemfile /myapp/Gemfile && \  
# cp /tmp/goat/Gemfile.lock /myapp/Gemfile.lock && \  
# cd /myapp && \  
# bundle install  
  
#RUN mv /tmp/goat/* . && \  
# rm -Rf /tmp/goat  
  
EXPOSE 3000  
  
  

