FROM bigtruedata/scala:2.12.4  
RUN wget -O- "https://piccolo.link/sbt-1.1.4.tgz" \  
| tar xzf - -C /usr/local \--strip-components=1 \  
&& sbt exit  
  
RUN curl -L -o /usr/local/bin/amm
https://github.com/lihaoyi/Ammonite/releases/1.1.0/2.12-1.1.0 \  
&& chmod +x /usr/local/bin/amm  
  
CMD ["amm"]  

