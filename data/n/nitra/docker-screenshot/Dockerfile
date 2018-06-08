FROM andrewpro/phantomjs  
  
# Add imagemagick  
RUN apt-get update && apt-get install -y \  
imagemagick jq \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
COPY r.js .  
COPY main.sh .  
  
CMD ["/main.sh"]  

