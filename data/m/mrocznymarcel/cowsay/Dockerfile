FROM debian  
RUN apt-get update && apt-get install -y cowsay fortune  
COPY entrypoint.sh /  
RUN ["chmod", "+x", "/entrypoint.sh"]  
ENV PATH $PATH:/usr/games  
ENTRYPOINT ["/entrypoint.sh"]

