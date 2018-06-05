FROM ubuntu:16.04  
MAINTAINER finios  
  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get -y install wget python git xz-utils imagemagick xdg-utils  
RUN rm /tmp/calibre* -Rf 2>&1 >/dev/null && wget -nv -O-
https://download.calibre-ebook.com/linux-installer.py | python -c "import sys;
main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read());
main()"  
  
WORKDIR /opt/calibre  
  
RUN mkdir -p /calibre-lib  
COPY server-users.sqlite /users.sqlite  
  
VOLUME ["/calibre-lib"]  
EXPOSE 8080  
ENV PREFIX /  
ENV LIBRARY /calibre-lib  
ENV AUTH disable-auth  
ENV BANAFTER 5  
ENV BANFOR 30  
ENV AJAXTIMEOUT 60  
ENV TIMEOUT 120  
ENV NUMPERPAGE 50  
ENV MAXOPDS 30  
CMD /opt/calibre/calibre-server --ban-after=$BANAFTER \--ban-for=$BANFOR
\--ajax-timeout=$AJAXTIMEOUT \--timeout=$TIMEOUT \--num-per-page=$NUMPERPAGE
\--max-opds-items=$MAXOPDS \--url-prefix=$PREFIX \--userdb /users.sqlite
--$AUTH \--port=8080 $LIBRARY  

