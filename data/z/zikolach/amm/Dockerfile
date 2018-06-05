FROM java  
RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends less  
ADD hello.scala /  
RUN mkdir ~/.ammonite && curl -Ls -o ~/.ammonite/predef.scala
https://git.io/vro0a  
RUN curl -Ls -o /bin/amm https://git.io/vro0u && chmod +x /bin/amm && amm
hello.scala 2>/dev/null && rm hello.scala  
CMD ["amm"]  

