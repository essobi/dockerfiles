FROM jess/slack  
  
RUN useradd user  
  
RUN apt-get update && apt-get install -y wget  
RUN wget https://github.com/meyskens/x-www-browser-
forward/releases/download/0.0.1/client && \  
mv client /usr/bin/x-www-browser && \  
chmod +x /usr/bin/x-www-browser  
  
USER user  
ENTRYPOINT ["/usr/bin/slack"]  
  

