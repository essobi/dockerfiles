FROM masm/nodejs  
MAINTAINER Marco Monteiro <marco@neniu.org>  
  
EXPOSE 80  
  
RUN pacman -Sqy --needed --noconfirm --noprogressbar \  
ghostscript \  
imagemagick \  
ffmpeg \  
faad2 \  
lame \  
mp3info \  
mplayer \  
pdfsam \  
pdftk \  
poppler \  
ttf-dejavu \  
unoconv && \  
yes | pacman -Sqcc && \  
rm -rf /usr/share/man/*  

