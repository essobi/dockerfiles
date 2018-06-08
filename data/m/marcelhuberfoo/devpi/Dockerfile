FROM marcelhuberfoo/arch  
  
MAINTAINER Marcel Huber <marcelhuberfoo@gmail.com>  
  
USER root  
  
RUN pacman -Syyu --noconfirm && \  
pacman-db-upgrade && \  
pacman -S --noconfirm sqlite3 python && \  
printf "y\\\ny\\\n" | pacman -Scc  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
RUN mkdir -p -m 0775 /data && chown -R $UNAME:$GNAME /data  
  
ADD https://raw.github.com/pypa/pip/master/contrib/get-pip.py /get-pip.py  
RUN python /get-pip.py  
RUN pip install devpi-server devpi-client devpi-web certifi  
  
VOLUME ["/data"]  
ENV DEVPI_CLIENTDIR=/tmp/devpi-client \  
DEVPI_SERVERDIR=/data \  
DEVPI_SERVER_OPTIONS="--host=0.0.0.0 --port=3141"  
EXPOSE 3141  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["dummy"]  
  

