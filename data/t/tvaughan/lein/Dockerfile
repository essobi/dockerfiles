FROM tvaughan/openjdk-jdk:8  
MAINTAINER "Tom Vaughan <tvaughan@tocino.cl>"  
RUN curl -sL -o /usr/local/bin/lein
https://raw.githubusercontent.com/technomancy/leiningen/2.6.1/bin/lein \  
&& chmod a+x /usr/local/bin/lein  
  
ENV LEIN_HOME /srv/lein  
ENV LEIN_ROOT 1  
ENV LEIN_REPL_HOST 0.0.0.0  
ENV LEIN_REPL_PORT 5309  
EXPOSE $LEIN_REPL_PORT  
  
CMD ["lein"]  

