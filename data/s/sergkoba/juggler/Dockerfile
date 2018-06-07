FROM elixir:1.4.0  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install Docker client  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install hex  
RUN mix local.hex --force  
  
# Install rebar  
RUN mix local.rebar --force  
  
# Install the Phoenix framework itself  
RUN mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez  
  
# Install NodeJS 6.x and the NPM  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y -q nodejs  
  
# Set /app as workdir  
WORKDIR /app  

