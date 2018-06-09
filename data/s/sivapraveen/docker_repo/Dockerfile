FROM ruby:2.3.0  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends mysql-server tcl && \  
apt-get install --no-install-recommends -y -q curl python build-essential git
ca-certificates && \  
apt-get install -y libgmp3-dev && \  
apt-get clean  
  
RUN apt-get -qq -y install build-essential wget  
  
COPY /scripts/setup/chruby.sh /scripts/setup/chruby.sh  
  
RUN /scripts/setup/chruby.sh  
  
# installation of ruby-install  
COPY /scripts/setup/ruby-install.sh /scripts/setup/ruby-install.sh  
RUN /scripts/setup/ruby-install.sh  
  
# setting up rubies  
COPY /scripts/setup/rubies.sh /scripts/setup/rubies.sh  
RUN /scripts/setup/rubies.sh  
  
# final execution bit  
COPY /scripts/exec/run.sh /scripts/exec/run.sh  
CMD /scripts/exec/run.sh  
  
MAINTAINER Siva Praveen <rsivapraveen001@gmail.com>

