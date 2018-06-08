FROM geoder101/fsharp-extended:1.0  
MAINTAINER George Dernikos <geoder101@gmail.com>  
  
COPY hooks/ /usr/local/bin/  
RUN mkdir -p /app/src /app/dist  
WORKDIR /app/src  
  
ONBUILD COPY . .  
ONBUILD RUN app-env-init \  
&& app-build \  
&& app-install  
  
CMD ["app-run"]  

