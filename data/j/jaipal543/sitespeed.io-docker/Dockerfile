FROM sitespeedio/webbrowsers:firefox-54.0-chrome-60.0  
COPY start.sh /start.sh  
  
RUN apt-get update  
  
RUN apt-get install -y git  
  
RUN addgroup --system --gid 2718 ppoker && \  
adduser --system --uid 2718 --gid 2718 --home /home/ppoker ppoker  
  
ENV HOME=/home/ppoker  
  
RUN git clone https://github.com/sitespeedio/sitespeed.io.git
$HOME/sitespeed.io  
  
RUN chown -R ppoker:ppoker $HOME/*  
  
USER ppoker  
  
WORKDIR $HOME/sitespeed.io  
  
RUN npm install --production  
  
ENTRYPOINT ["/start.sh"]  
VOLUME /sitespeed.io  
WORKDIR /sitespeed.io  

