FROM debian  
  
RUN apt-get update && apt-get install -y git curl webp fontconfig libicu-dev  
RUN git clone \--depth 1 https://github.com/astefanutti/decktape.git  
WORKDIR /decktape  
RUN curl -L http://astefanutti.github.io/decktape/downloads/phantomjs-linux-
debian8-x86-64 -o bin/phantomjs  
RUN chmod +x bin/phantomjs  
  
ENTRYPOINT ["/decktape/bin/phantomjs", "decktape.js"]  
CMD ["-h"]  
  

