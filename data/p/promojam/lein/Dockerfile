FROM promojam/oracle-jdk:1.8.0_31  
  
ENV LEIN_VERSION 2.5.1  
ENV LEIN_ROOT 1  
ENV HTTP_CLIENT curl -k -s -f -L -o  
  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
https://raw.githubusercontent.com/technomancy/leiningen/$LEIN_VERSION/bin/lein
\  
\--output /usr/bin/lein \  
&& chmod 0755 /usr/bin/lein  
  
RUN opkg-install bash ; /usr/bin/lein upgrade  
  
VOLUME [ "/app" ]  
WORKDIR /app  
ENTRYPOINT ["lein"]  

