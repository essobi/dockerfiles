FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y pandoc texlive-xetex fontconfig  
  
RUN mkdir /root/.fonts/  
COPY *.ttf /root/.fonts/  
  
RUN fc-cache -fv  

