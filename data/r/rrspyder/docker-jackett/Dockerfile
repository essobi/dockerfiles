FROM mono  
MAINTAINER RRSpyder <rrspyder@gmail.com>  
  
WORKDIR /usr/local/src  
RUN curl -LOs $(curl -s https://api.github.com/repos/Jackett/Jackett/releases
| grep "browser_download_url" | grep "Mono" | cut -d '"' -f 4 | sort -V
--reverse | head -1)  
RUN tar -xzf Jackett*.tar.gz  
RUN mkdir -p /data/app  
RUN mkdir -p /data/config  
RUN mv ./Jackett /data/app/  
RUN chown -R nobody:users /data/app  
RUN chown -R nobody:users /data/config  
RUN ln -s /data/config /usr/share/Jackett  
RUN rm -rf /usr/local/src/*  
  
EXPOSE 9117  
VOLUME /data/config  
VOLUME /data/app  
  
ADD files/start.sh /  
RUN chmod +x /start.sh  
  
WORKDIR /data/app/Jackett  
  
ENTRYPOINT ["mono", "JackettConsole.exe"]  

