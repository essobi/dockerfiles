FROM gdoteof/yesod-init  
  
RUN apt-get update && apt-get install -y libpq-dev  
  
ENV HOME /root  
  
ENV PATH /root/.cabal/bin:$PATH  
  
RUN mkdir scratch  
  
#force dependency grab for yesod scaffolded with postgres support  
WORKDIR /scratch  
  
RUN printf %s\\\n 'scaffold' 'p' | yesod init  
  
RUN cd scaffold && cabal install --enable-tests . --max-backjumps=-1
--reorder-goals  
  

