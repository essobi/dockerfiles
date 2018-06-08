FROM clojure:lein-2.7.1  
LABEL maintainer "Luo Tian (@robortluo)"  
  
WORKDIR /opt  
RUN \  
curl -fsSLo phantomjs.tar.bz2
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
tar xvf phantomjs.tar.bz2 && \  
rm phantomjs.tar.bz2 && \  
ln -s phantomjs-2.1.1-linux-x86_64 phantomjs  
ENV PATH="${PATH}:/opt/phantomjs/bin"  
COPY lein_profile.clj /root/.lein/profiles.clj  
CMD phantomjs

