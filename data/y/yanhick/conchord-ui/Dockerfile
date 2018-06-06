FROM ubuntu:14.10  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:hvr/ghc  
RUN apt-get update && apt-get install -y \  
cabal-install-1.20 \  
ghc-7.8.4 \  
git \  
wget \  
curl \  
python \  
build-essential \  
ruby-dev \  
zlib1g-dev  
  
RUN gem install compass  
  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get install -y nodejs  
  
# Needed by some hackage libs  
ENV LANG C.UTF-8  
# Add GHC and Cabal to PATH  
ENV PATH /opt/cabal/1.20/bin:/opt/ghc/7.8.4/bin:/.cabal/bin:$PATH  
ENV HOME /home  
  
# Get code  
RUN git clone https://github.com/yanhick/conchord-ui.git /conchord  
WORKDIR /conchord  
  
# Build client  
RUN npm install  
RUN ./node_modules/bower/bin/bower install --allow-root  
RUN ./node_modules/.bin/gulp dev  
  
# Build server  
RUN cabal update  
RUN cabal install -j4 alex happy  
RUN cabal install -j4 --only-dependencies  
RUN cabal configure && cabal build -j4  
  
ENV PORT 80  
EXPOSE 80  
RUN mv dist/ /opt  
WORKDIR /opt  
  
# Start server  
CMD /opt/dist/build/conchord-ui/conchord-ui  
  
# Clean up  
RUN apt-get remove -y \  
cabal-install-1.20 \  
ghc-7.8.4 \  
git \  
wget \  
curl \  
python \  
build-essential \  
ruby-dev \  
zlib1g-dev  
  
RUN rm -rf /conchord  

