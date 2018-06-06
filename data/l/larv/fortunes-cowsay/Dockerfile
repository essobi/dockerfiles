FROM ubuntu:14.04  
RUN apt-get -y update \  
&& apt-get install -y --no-install-recommends fortunes-ru cowsay \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN locale-gen ru_RU.UTF-8  
ENV LC_ALL ru_RU.UTF-8  
ENV LANG ru_RU.UTF-8  
ENV LANGUAGE ru_RU:ru  
  
ENV PATH $PATH:/usr/games  
  
COPY docker.cow /usr/share/cowsay/cows/  
COPY fortune-cowsay.sh /usr/games/  
RUN ln -sv /usr/games/fortune-cowsay.sh /usr/games/fortune-cowsay  
  
CMD fortune-cowsay  

