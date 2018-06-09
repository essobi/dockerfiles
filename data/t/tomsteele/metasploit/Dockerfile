FROM ruby:2.1.6  
MAINTAINER Tom Steele <tom@stacktitan.com>  
  
WORKDIR /root  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get -y install build-essential libreadline-dev libssl-dev libpq5
libpq-dev libreadline5 libsqlite3-dev libpcap-dev openjdk-7-jre git-core
autoconf curl zlib1g-dev libxml2-dev libxslt1-dev vncviewer libyaml-dev curl  
  
RUN svn co https://svn.nmap.org/nmap  
WORKDIR /root/nmap  
RUN ./configure && make && make install && make clean  
  
WORKDIR /root  
RUN git clone https://github.com/rapid7/metasploit-framework.git  
WORKDIR /root/metasploit-framework  
RUN bundle install  
  
CMD ["./msfconsole"]  

