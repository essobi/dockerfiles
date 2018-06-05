FROM wonderbeat/yesod  
MAINTAINER Denis Golovachev <borov.htid@gmail.com>  
  
RUN apt-get install git -qy libpq-dev  
RUN git clone https://github.com/TimeAttack/time-attack-server.git  
RUN cd time-attack-server && cabal sandbox init && cabal install --enable-
tests --only-dependencies  

