FROM heroku/cedar:14  
MAINTAINER Joe Ferris <jferris@thoughtbot.com>  
ENV LANG en_US.UTF-8  
RUN mkdir /deb  
RUN cd /deb \  
&& wget --quiet \  
https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \  
&& dpkg -i erlang-solutions_1.0_all.deb  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
erlang \  
erlang-dev \  
erlang-doc \  
erlang-src \  
elixir  
  
CMD iex  

