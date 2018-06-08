FROM python:slim  
  
WORKDIR /workdir  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y build-essential libffi-dev lame curl  
  
RUN curl -L -o libspotify.tar.gz
https://www.dropbox.com/s/bdug65yx4kgepl2/libspotify-12.1.51-Linux-x86_64-release.tar.gz?dl=1  
RUN tar xvf libspotify.tar.gz  
RUN cd ./libspotify-12.1.51-Linux-x86_64-release && \  
make install prefix=/usr/local  
  
RUN pip install --upgrade pip
https://www.dropbox.com/s/w6tisv56jzs9fk4/spotify-ripper-2.10.5.tar.gz?dl=1  
  
RUN printf "[main]\n \  
last = True\n \  
directory = /workdir\n \  
format = {track_name}_{artist}.{ext}\n \  
quality = 320\n \  
bitrate = 320\n \  
cbr = CBR\n \  
normalize = False \n \  
key = /workdir/spotify_appkey.key \n \  
timeout = 3600 \n \  
" > /root/.spotify-ripper/config.ini  
  
ENTRYPOINT ["spotify-ripper"]  

