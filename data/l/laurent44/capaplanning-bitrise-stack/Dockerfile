FROM bitriseio/docker-bitrise-base:latest  
  
# Important! Update this no-op ENV variable when this Dockerfile  
# is updated with the current date. It will force refresh of all  
# of the base images and things like `apt-get update` won't be using  
# old cached versions when the Dockerfile is built.  
ENV REFRESHED_AT=2018-02-01  
RUN echo "deb http://packages.erlang-solutions.com/ubuntu trusty contrib" >>
/etc/apt/sources.list \  
&& apt-key adv --fetch-keys http://packages.erlang-
solutions.com/ubuntu/erlang_solutions.asc \  
&& apt-get -qq update \  
# Install Elixir  
&& apt-get install -y erlang-dev erlang-parsetools elixir inotify-tools \  
# Cleanup  
&& apt-get clean  
  
# Install local Elixir hex and rebar  
RUN /usr/local/bin/mix local.hex --force && \  
/usr/local/bin/mix local.rebar --force  
  
RUN elixir -v  
RUN node --version  
RUN npm --version  
  
# Install Google Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" >> /etc/apt/sources.list.d/google.list'  
RUN apt-get update && apt-get install -y google-chrome-stable  

