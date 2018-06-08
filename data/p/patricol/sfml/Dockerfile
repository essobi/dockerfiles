FROM patricol/cpp:18.04  
  
USER root  
  
RUN apt-get update; \  
apt-get install -y libsfml-dev && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV LIB=/usr/lib  
ENV INCLUDE=/usr/include/SFML  
  
  
USER user

