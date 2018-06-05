FROM thor/debian-console  
  
RUN apt-get -y install ffmpeg  
  
RUN mkdir /works  
WORKDIR /works  
  
COPY script.sh /works/  
CMD ["sh", "-c", "/works/script.sh"]  

