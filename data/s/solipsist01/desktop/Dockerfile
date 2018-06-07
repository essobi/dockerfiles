FROM dorowu/ubuntu-desktop-lxde-vnc  
  
RUN \  
apt-get \--assume-yes update && \  
apt-get \--assume-yes install apt-transport-https wget && \  
wget -q -O - https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt | sudo apt-
key add \- && \  
add-apt-repository 'deb https://mkvtoolnix.download/ubuntu xenial main' && \  
add-apt-repository ppa:stebbins/handbrake-git-snapshots -y && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/ubuntu xenial main" | sudo tee
/etc/apt/sources.list.d/mono-official.list && \  
apt-get \--assume-yes update && apt-get install --assume-yes mono-complete
gtk-sharp2 gnome-commander mkvtoolnix mkvtoolnix-gui handbrake-gtk handbrake-
cli yasm fslint ssh && \  
wget http://ffmpeg.mplayerhq.hu/releases/ffmpeg-2.6.2.tar.bz2 && \  
tar -xjvf ffmpeg-2.6.2.tar.bz2 && \  
cd ffmpeg-2.6.2/ && \  
./configure && \  
make && \  
make install && \  
wget http://www.wenro.nl/gemistdownloader.deb && \  
dpkg -i gemistdownloader.deb  

