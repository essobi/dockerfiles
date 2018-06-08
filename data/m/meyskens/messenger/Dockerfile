FROM meyskens/desktop-base:latest  
  
RUN apt-get update &&\  
apt-get -y install libappindicator1 gconf2 python gvfs-bin xdg-utils libcap2  
  
RUN wget https://github.com/aluxian/Messenger-for-
Desktop/releases/download/v2.0.9/messengerfordesktop-2.0.9-linux-amd64.deb &&\  
dpkg -i messengerfordesktop-2.0.9-linux-amd64.deb && rm *.deb  
  
CMD /usr/bin/messengerfordesktop

