FROM library/elixir:1.3.4  
MAINTAINER kelu <kelostrada@gmail.com>  
  
RUN apt-get -y update  
  
# Install dependencies  
RUN apt-get -y install curl postgresql-client  
  
# Install NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get install -y nodejs  
  
# Install Hex  
RUN mix local.hex --force  
  
# Install Rebar  
RUN mix local.rebar --force  
  
# Install Phoenix-Framework package  
RUN mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new-1.2.1.ez
--force

