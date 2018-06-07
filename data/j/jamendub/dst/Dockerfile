FROM jamendub/steam  
  
RUN apt-get update && apt-get install -y libcurl4-gnutls-dev:i386 lib32stdc++6  
  
VOLUME /dst/cluster  
  
COPY cluster /dst/cluster  
COPY run.sh /dst  
  
WORKDIR /dst  
  
CMD ./run.sh  

