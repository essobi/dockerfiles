FROM gliderlabs/alpine:3.1  
RUN apk --update add \  
git \  
python  
  
RUN git clone https://github.com/drzoidberg33/plexpy.git /opt/plexpy  
  
VOLUME /data  
  
EXPOSE 8181  
WORKDIR /opt/plexpy  
  
CMD ["/usr/bin/python", "PlexPy.py", "--datadir=/data"]  

