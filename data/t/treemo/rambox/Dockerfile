FROM debian  
  
  
# Add non privileged user  
RUN useradd -m user  
  
# install requirements  
RUN apt update  
RUN apt upgrade -y  
RUN apt install -y wget libgtk2.0-0 libx11-xcb1 libxtst6 libxss1 libgconf-2-4
libnss3 libasound2  
  
# install app  
WORKDIR /tmp  
RUN wget https://api.github.com/repos/saenzramiro/rambox/releases/latest  
RUN wget $(grep 'https' latest | grep '\\.deb' | grep $(dpkg --print-
architecture | grep -o '[0-9]\\+') | cut -d '"' -f 4)  
RUN dpkg --force-depends -i *.deb  
RUN apt -f install -y  
  
# clean / optimise docker size  
RUN apt remove --purge -y wget  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/* /var/tmp/*  
  
# running  
USER user  
ENTRYPOINT rambox  
  

