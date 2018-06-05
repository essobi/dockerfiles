FROM ubuntu:14.04  
MAINTAINER janes <miscjanes@gmail.com>  
  
# Set default locale for the environment  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
git \  
libsqlite3-dev \  
software-properties-common sqlite3 \  
&& apt-add-repository -y ppa:brightbox/ruby-ng \  
&& apt-get update \  
&& apt-get install -y \  
ruby2.2 \  
ruby2.2-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install bundler  
  
WORKDIR /opt  
  
RUN git clone git://github.com/beefproject/beef.git  
  
WORKDIR /opt/beef  
  
RUN bundle install  
  
EXPOSE 3000  
CMD ["./beef"]  
  

