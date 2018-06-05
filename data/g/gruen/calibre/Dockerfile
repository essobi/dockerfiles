FROM ubuntu  
  
LABEL Darren Green "<darren@gruen.site>"  
  
RUN apt-get update \  
&& apt-get install -y calibre \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get autoremove -y  
  
WORKDIR /root/books  
  
VOLUME ["/root/books", "/root/Downloads", "/root/Documents"]  
  
ENTRYPOINT [ "calibre" ]  
  
CMD ["--with-library", "/root/books"]  

