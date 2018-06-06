FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y curl tmux nginx ffmpeg python3 python3-urwid nodejs npm  
  
COPY ext /ext  
COPY carillon /ext/lib/carillon  
  
CMD /ext/bin/carillon-init  
  
EXPOSE 8080  
EXPOSE 8081  

