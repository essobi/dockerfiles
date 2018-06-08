FROM garage/base  
  
MAINTAINER Reinaldo Junior <juniorz@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
  
## Installs Erlang from Erlang Solutions  
RUN curl -q http://packages.erlang-solutions.com/debian/erlang_solutions.asc |
apt-key add - &&\  
echo "deb http://packages.erlang-solutions.com/debian $(/var/garage/base-
release) contrib" > /etc/apt/sources.list.d/erlang-solutions.list &&\  
apt-get update &&\  
/var/garage/install esl-erlang  
  
## Installs rebar  
RUN /var/garage/install git &&\  
git clone git://github.com/rebar/rebar.git /tmp/rebar &&\  
cd /tmp/rebar && ./bootstrap &&\  
mv ./rebar /usr/local/bin/ &&\  
chmod 0755 /usr/local/bin/rebar  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV GARAGE_PROVIDES erl erlc rebar

