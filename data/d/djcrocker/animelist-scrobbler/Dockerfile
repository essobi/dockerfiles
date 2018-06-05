FROM golang  
  
ADD . /go/src/github.com/djcrock/animelist-scrobbler  
  
RUN go get github.com/djcrock/animelist-scrobbler  
  
EXPOSE 8080/tcp  
  
ENTRYPOINT /go/bin/animelist-scrobbler -maluser $MAL_USER -malpass $MAL_PASS
-plexurl $PLEX_URL -plextoken $PLEX_TOKEN -plexuser $PLEX_USER  

