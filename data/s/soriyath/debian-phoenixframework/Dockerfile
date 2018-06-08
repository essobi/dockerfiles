FROM soriyath/debian-nodejs5  
MAINTAINER Sumi Straessle  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /usr/local/src  
  
# Install Erlang and Elixir  
RUN apt-get update \  
&& apt-get install -y apt-transport-https  
  
RUN wget https://packages.erlang-solutions.com/debian/erlang_solutions.asc \  
&& apt-key add erlang_solutions.asc \  
&& echo "deb https://packages.erlang-solutions.com/debian wheezy contrib" >>
/etc/apt/sources.list.d/erlang.list \  
&& apt-get update \  
&& apt-get install -y --fix-missing esl-erlang inotify-tools lksctp-tools  
  
# Compile elixir v 1.3.3  
RUN mkdir elixir-1.3.3 \  
&& cd elixir-1.3.3 \  
&& wget https://github.com/elixir-
lang/elixir/releases/download/v1.3.3/Precompiled.zip \  
&& unzip Precompiled.zip \  
&& rm Precompiled.zip  
  
ENV PATH "/usr/local/src/elixir-1.3.3/bin:$PATH"  
# Install Phoenix Framework  
RUN mix local.hex \  
&& mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez  
RUN npm install -g brunch \  
&& npm install  
  
# Clean  
RUN apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 4000  
WORKDIR /srv/www  
  
CMD supervisord -c /etc/supervisor.conf  

