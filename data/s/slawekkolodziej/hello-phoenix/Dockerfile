FROM elixir:latest  
  
RUN apt-get update && apt-get install -y curl  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  
  
# RUN ln -s /usr/bin/nodejs /usr/bin/node  
# Set application dir  
ENV APP_HOME /app  
  
# Install phoenix  
RUN mix archive.install --force \  
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez  
  
# Install hex and rebar  
RUN mix local.hex --force  
RUN mix local.rebar --force  
  
# Create application directory, add application files there and set it as
workdir  
RUN mkdir $APP_HOME  
ADD . $APP_HOME  
WORKDIR $APP_HOME  
  
# Install dependencies  
RUN mix deps.get --force  
  
# Compile the app  
RUN mix do hex.info, compile  
  
# Install node modules  
# RUN npm set progress=false && npm install -g brunch && npm install  
# Run server  
EXPOSE 4000  
CMD ["mix", "phoenix.server"]  

