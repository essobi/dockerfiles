FROM pushbit/ruby  
  
MAINTAINER Luke Roberts "email@luke-roberts.co.uk"  
# Update aptitude with new repo  
RUN apt-get update  
  
# Install software  
RUN apt-get install -y git  
RUN apt-get install -y wget  
RUN apt-get install -y build-essential  
RUN apt-get install -y sqlite3  
RUN apt-get install -y libsqlite3-dev  
RUN apt-get install -y libxslt-dev  
RUN apt-get install -y libxml2-dev  
  
RUN gem install bundler  
RUN gem install tilt  
RUN gem install faraday  
RUN gem install sanitize  
  
RUN touch Gemfile  
  
ADD ./execute.sh ./execute.sh  
ADD ./app ./app  
  
CMD ["./execute.sh"]

