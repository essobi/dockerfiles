FROM haskell:7.10  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install zlib1g-dev libssl-dev -y  
RUN apt-get install git -y  
  
ENV LANG en_US.utf8  
  
RUN cabal update  
  
# Include Dev webhooks types  
RUN echo "redo webhooks pul"  
RUN git clone https://github.com/ChristopherBiscardi/webhooks.git
$HOME/webhooks  
#ADD ./webhooks $HOME/webhooks  
#RUN cd $HOME/webhooks && cabal install  
# END Dev webhooks types  
ADD ./server $HOME/server  
  
WORKDIR $HOME/server  
RUN cabal sandbox init && cabal sandbox add-source $HOME/webhooks  
  
RUN cabal install --only-dependencies -j4  
  
RUN cabal build  
  
#CMD ["/root/.cabal/bin/bot","--no-access-log","--no-error-log"]  
CMD ["/root/server/dist/build/bot/bot","--no-access-log","--no-error-log"]  

