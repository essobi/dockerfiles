FROM meyskens/desktop-base  
  
RUN apt-get update && apt-get install -y \  
zenity \  
libgnome-keyring0 \  
gir1.2-gnomekeyring-1.0 \  
git \  
gconf2 \  
python \  
gvfs-bin \  
xdg-utils \  
libgnome-keyring-dev  
  
RUN wget -O mail.deb "https://edgehill.nylas.com/download?platform=linux-deb"
&& \  
dpkg -i mail.deb && \  
rm -f mail.deb  
  
CMD nylas-mail

