FROM marvambass/nodejs  
MAINTAINER MarvAmBass  
  
RUN apt-get update; apt-get install -y \  
unzip \  
curl \  
pwgen  
  
ENV NODE_ENV production  
  
RUN wget https://ghost.org/zip/ghost-latest.zip -O ghost.zip && \  
unzip -uo ghost.zip -d /ghost && rm ghost.zip && \  
bash -c 'source /root/.nvm/nvm.sh && cd /ghost && npm install --production'  
  
RUN cp -a /ghost/content /ghost/content.bak  
  
WORKDIR /ghost  
  
ADD startup-ghost.sh /opt/startup-ghost.sh  
RUN chmod a+x /opt/startup-ghost.sh  
  
RUN sed -i 's/# exec CMD/# exec CMD\n\/opt\/startup-ghost.sh/g'
/opt/entrypoint.sh  
  
EXPOSE 2368  

