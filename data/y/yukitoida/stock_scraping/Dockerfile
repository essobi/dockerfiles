FROM elixir  
MAINTAINER yuki-toida  
  
RUN apt-get update  
  
# hex  
RUN mix local.hex --force && \  
mix local.rebar --force && \  
mix hex.info  
  
# phoenix  
RUN mix archive.install
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez  
  
# node npm  
RUN apt-get install -y nodejs npm  
RUN npm cache clean && npm install n -g  
RUN n stable && ln -sf /usr/local/bin/node /usr/bin/node  
RUN apt-get purge -y nodejs npm  
  
# inotify-tools  
RUN apt-get install -y inotify-tools  
  
EXPOSE 4000  
# git repository  
RUN git clone https://github.com/yuki-toida/stock_scraping.git
root/stock_scraping  
WORKDIR /root/stock_scraping  
RUN chmod +x run.sh  
ENTRYPOINT ["./run.sh"]  
CMD ["dev"]  

