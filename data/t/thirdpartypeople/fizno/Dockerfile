FROM ubuntu:precise  
MAINTAINER Michiel de Jong "michiel@unhosted.org"  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y python-software-properties python g++  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
  
RUN apt-get install -y screen  
RUN mkdir knowledge  
RUN #screen -d -m -S wikipedia transmission-cli -w knowledge/
http://download.kiwix.org/portable/wikipedia_en_all_nopic.zip.torrent  
RUN #screen -d -m -S osm transmission-cli -w knowledge/ http://osm-
torrent.torres.voyager.hr/files/planet-140131.osm.bz2.torrent &  
RUN #screen -d -m -S ubuntu transmission-cli -w knowledge/
http://torrent.ubuntu.com:6969/file?info_hash=Yz%92%F6%EE%ED%29%E6%02%8Bp%B4%16%C8G%E5%1B%A7l8
&  
RUN #screen -d -m -S khan transmission-cli -w knowledge/
magnet:?xt=urn:btih:b954f79f319b1d51d54068e90ca2f64b5c491b45&&dn=Khan+Academy+-+Complete+Set+-+480x272+-+7.+Aug.+2011&&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&&tr=udp%3A%2F%2Fopen.demonii.com%3A1337
&  
RUN #screen -d -m -S coursera transmission-cli -w knowledge/
magnet:?xt=urn:btih:450605cb6104c8adbcfd443ddac76eb2fd709bf1&&dn=Coursera.org+-+A+History+of+the+World+Since+1300&&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&&tr=udp%3A%2F%2Fopen.demonii.com%3A1337
&  
RUN #screen -d -m -S gutenberg transmission-cli -w knowledge/
http://snowy.arsc.alaska.edu/cdproject/torrents/pgdvd042010.iso.torrent &  
RUN #screen -d -m -S english transmission-cli -w knowledge/
magnet:?xt=urn:btih:f4482dd7f8b28b37f1c5e4328cd94778d1fdc43d&&dn=English+mp3+files+with+transcripts++%28British+Council%29+Perfect&&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&&tr=udp%3A%2F%2Fopen.demonii.com%3A1337
&  
RUN #screen -d -m -S udhr transmission-cli -w knowledge/
magnet:?xt=urn:btih:51368b2d31dde2788667aba6edb8c10d16d05c9b&&dn=The+Universal+Declaration+of+Human+Rights&&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&&tr=udp%3A%2F%2Ftracker.publicbt.com%3A80&&tr=udp%3A%2F%2Ftracker.istole.it%3A6969&&tr=udp%3A%2F%2Ftracker.ccc.de%3A80&&tr=udp%3A%2F%2Fopen.demonii.com%3A1337
&  
  
RUN echo "deb http://www.robertix.com/telechargements/binaires/ ./" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y --force-yes kiwix  
  
ADD . ./fizno  
RUN cd fizno && npm install  
  
EXPOSE 49080  
CMD cd fizno && node ./docker.js  

