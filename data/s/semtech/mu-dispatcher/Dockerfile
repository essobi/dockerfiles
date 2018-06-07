FROM madnificent/elixir-server:latest  
  
RUN sed -i "2i\\\cp /config/dispatcher.ex /app/lib/dispatcher.ex" /startup.sh  
  
ADD . /app  
  
RUN sh /setup.sh  

