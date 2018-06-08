FROM musite/gregorio  
  
RUN apt-get -y install git python3 python3-matplotlib python3-distutils  
  
# Configuration de git  
RUN git config --global user.email "musite@localhost" && \  
git config --global user.name "Musite"  
  
# Installation du site  
RUN cd /opt && \  
git clone \--depth=1 https://github.com/musite-project/musite && \  
mkdir /opt/musite/data /opt/musite/etc && \  
mkdir /usr/share/fonts/perso  
  
VOLUME
["/opt/musite/data","/opt/musite/static/docs","/opt/musite/etc","/usr/share/fonts/perso"]  
  
ADD serveur.sh /opt/musite/serveur.sh  
  
EXPOSE 80  
CMD ["/opt/musite/serveur.sh"]  

