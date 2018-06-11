FROM masm/nodejs  
MAINTAINER Marco Monteiro <marco@neniu.org>  
  
EXPOSE 80  
  
RUN pacman -Sqy --needed --noconfirm --noprogressbar \  
ruby \  
ttf-dejavu \  
wkhtmltopdf-static \  
zip && \  
yes | pacman -Sqcc && \  
rm -rf /usr/share/man/*  

