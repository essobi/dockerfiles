FROM alpine  
  
ADD http://equine.vacantminded.com/~kabaka/kabaka-529bc4fa.rsa.pub
/etc/apk/keys/  
ADD repositories /etc/apk/  
ADD mpdconf /app/mpdconf  
  
RUN apk update && apk add mpd-kabaka  
  
CMD mpd --no-daemon /app/mpdconf  
  
EXPOSE 6600  
EXPOSE 8000  
RUN mkdir -p /app/playlists && cd /app && touch database log pid state
sticker.sql  

