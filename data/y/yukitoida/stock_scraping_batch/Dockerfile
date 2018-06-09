FROM elixir  
MAINTAINER yuki-toida  
  
RUN mix local.hex --force && \  
mix local.rebar --force && \  
mix hex.info  
  
RUN git clone https://github.com/yuki-toida/stock_scraping_batch.git
root/stock_scraping_batch  
  
WORKDIR /root/stock_scraping_batch  
  
RUN chmod +x run.sh  
  
ENTRYPOINT ["./run.sh"]  
  
CMD ["dev"]  

