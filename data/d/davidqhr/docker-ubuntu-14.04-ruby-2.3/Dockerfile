FROM ubuntu:14.04  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update  
  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:brightbox/ruby-ng  
RUN apt-get update  
  
RUN apt-get install -y ruby2.3 ruby2.3-dev  
RUN apt-get install -y imagemagick libmagickwand-dev  
RUN apt-get install -y libmysqlclient-dev  
RUN apt-get install -y nodejs  
RUN apt-get install -y git  
RUN apt-get install -y build-essential  
RUN apt-get install -y libsqlite3-dev  
RUN apt-get install -y mysql-client  
RUN apt-get install -y libpq-dev  
RUN apt-get clean  
  
RUN gem install bundler  
  
# avoid warning: Don't run Bundler as root  
RUN bundle config \--global silence_root_warning 1  
  
# avoid warning: The git source `git://github.com/dwbutler/logstash-
logger.git` uses the `git` protocol, which transmits data without encryption.
Disable this warning with `bundle config git.allow_insecure true`, or switch
to the `https` protocol to keep your data secure.  
RUN bundle config \--global git.allow_insecure true  
# set timezone  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN locale-gen en_US.UTF-8  
RUN locale -a  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

