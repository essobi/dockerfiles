FROM ubuntu:16.04  
  
RUN apt-get update && apt-get install -y fortune cowsay lolcat  
  
ENV PATH /usr/games:${PATH}  
ENV LC_ALL=C  
  
ENTRYPOINT fortune | cowsay | lolcat  

