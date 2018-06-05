FROM starbuildr/phoenix-new:1.0.2  
MAINTAINER Vyacheslav Voronchuk <voronchuk@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y imagemagick  
RUN apt-get install -y mysql-client  
RUN apt-get install -y letsencrypt  
  
ARG MIX_ENV=prod  
ENV MIX_ENV $MIX_ENV  
  
WORKDIR /var/app  
  
# Software  
COPY ./web /var/app/web  
COPY ./config /var/app/config  
COPY ./priv /var/app/priv  
COPY ./lib /var/app/lib  
COPY ./mix.exs /var/app/mix.exs  
COPY ./mix.lock /var/app/mix.lock  
  
RUN mix deps.get --only prod && mix compile  
  
# Install Node Deps  
COPY ./brunch-config.js /var/app/brunch-config.js  
COPY ./package.json /var/app/package.json  
RUN npm install  
  
# Run Phoenix  
RUN brunch build --production  
RUN mix phoenix.digest  
  
ENTRYPOINT []  
CMD ["/bin/bash"]

