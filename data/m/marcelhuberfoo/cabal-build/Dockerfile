FROM marcelhuberfoo/arch  
  
MAINTAINER Marcel Huber <marcelhuberfoo@gmail.com>  
  
USER root  
  
RUN pacman -Syyu --noconfirm && \  
pacman-db-upgrade && \  
pacman -S --noconfirm ghc cabal-install && \  
printf "y\\\ny\\\n" | pacman -Scc  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
RUN mkdir -p -m 0775 /data /caballogs && chown -R $UNAME:$GNAME /data
/caballogs  
USER $UNAME  
RUN bash -l -c 'mkdir -p -m 0775 $HOME/.cabal && ln -s /caballogs
$HOME/.cabal/logs'  
  
VOLUME ["/data", "/caballogs"]  
WORKDIR /data  
  
RUN bash -l -c 'cabal update'  
USER root  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["cabal", "install", "-j"]  
  

