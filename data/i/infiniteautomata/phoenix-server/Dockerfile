# Phoenix Application Container  
FROM infiniteautomata/elixir-server  
MAINTAINER Carlos Killpack <carlos@infinite.ai>  
  
USER root  
RUN apt-get update > /dev/null && apt-get install nodejs npm inotify-tools >
/dev/null && ln -s /usr/bin/nodejs /usr/bin/node  
  
USER www-data  
RUN mix archive.install --force
https://github.com/phoenixframework/phoenix/releases/download/v0.13.1/phoenix_new-0.13.1.ez  

