FROM synology/lxqt:0.9.0  
MAINTAINER FrozenPK  
ENV GCRYPT libgcrypt11_1.5.3-2ubuntu4.3_amd64.deb  
ENV SPOT spotify-client-0.9.17_0.9.17.8.gd06432d.31-1_amd64.deb  
ENV PATHZ /workdir  
ENV DOWN downloads  
WORKDIR $PATHZ/$DOWN  
RUN wget
http://security.ubuntu.com/ubuntu/pool/main/libg/libgcrypt11/libgcrypt11_1.5.3-2ubuntu4.3_amd64.deb  
RUN dpkg -i ./$GCRYPT  
RUN wget https://dl.dropboxusercontent.com/u/8593574/Spotify/spotify-
client-0.9.17_0.9.17.8.gd06432d.31-1_amd64.deb  
RUN apt-get update && apt-get -y upgrade; exit 0  
RUN dpkg -i ./$SPOT; exit 0  
RUN apt-get update && apt-get -y -f install; exit 0  
RUN dpkg -i ./$SPOT  
RUN wget http://www.olejon.net/code/spotcommander/files/spotcommander-
latest.deb  
RUN apt-get update && apt-get -y upgrade; exit 0  
RUN dpkg -i ./spotcommander-latest.deb; exit 0  
RUN apt-get update && apt-get -y -f install; exit 0  
RUN dpkg -i ./spotcommander-latest.deb  
USER ubuntu  
RUN spotcommander start  
EXPOSE 50007:6080  
EXPOSE 50077:80

