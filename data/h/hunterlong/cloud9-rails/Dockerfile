#  
# Cloud9 IDE with Ruby on Rails and MySQL Client ready to go  
# Basically a mod of kdelfour/cloud9-docker found at:  
# https://github.com/kdelfour/cloud9-docker  
#  
FROM ruby:2.2  
MAINTAINER Hunter Long <info@socialeck.com>  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
  
# see http://guides.rubyonrails.org/command_line.html#rails-dbconsole  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 --no-install-recommends  
  
#
------------------------------------------------------------------------------  
# Install base  
RUN apt-get update && apt-get install -y build-essential g++ curl libssl-dev
apache2-utils git libxml2-dev sshfs  
  
#
------------------------------------------------------------------------------  
# Install Cloud9  
RUN git clone https://github.com/c9/core.git /cloud9  
WORKDIR /cloud9  
RUN scripts/install-sdk.sh  
  
COPY run.sh /cloud9/  
RUN chmod +x /cloud9/run.sh  
  
# Tweak standlone.js conf  
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js  
  
#
------------------------------------------------------------------------------  
# Add volumes  
RUN mkdir /workspace  
VOLUME /workspace  
VOLUME /usr/local/bundle  
  
#
------------------------------------------------------------------------------  
# Expose ports.  
EXPOSE 80  
EXPOSE 8080  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
ENV LOGIN_AUTH $LOGIN_AUTH  
ENV WORKSPACE_NAME $WORKSPACE_NAME  
  
ENTRYPOINT ["./run.sh"]  

