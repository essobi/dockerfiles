FROM elixir:latest  
  
WORKDIR /opt  
RUN wget -qO- https://github.com/tonini/alchemist-server/archive/master.tar.gz
| tar --transform 's/-master//' -xz  
  
WORKDIR /code  
ENTRYPOINT [ "elixir" ]  
CMD [ "/opt/alchemist-server/run.exs", "--env=dev", "--listen", "--port",
"50501" ]  
  

