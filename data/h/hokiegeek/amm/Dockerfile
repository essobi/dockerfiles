FROM hokiegeek/scala-sbt:latest  
  
RUN mkdir ~/.ammonite  
ADD predef.scala ~/.ammonite/predef.scala  
  
RUN curl -Ls -o /bin/amm
https://github.com/lihaoyi/Ammonite/releases/download/0.7.6/0.7.6 && chmod +x
/bin/amm  
RUN echo 'println("hw")' > hw.scala && /bin/amm hw.scala 2>/dev/null a && rm
-rf hw.scala  
  
ENTRYPOINT ["/bin/amm"]  

