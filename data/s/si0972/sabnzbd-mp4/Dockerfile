FROM binhex/arch-sabnzbd  
MAINTAINER si0972  
  
  
RUN \  
pacman -S --noconfirm \  
ffmpeg \  
git \  
python-pip \  
python \  
libxslt \  
libfdk-aac \  
cmake \  
make \  
gcc \  
qt5-base \  
qt5-tools && \  
  
pip install --upgrade pip && \  
pip install requests && \  
pip install requests[security] && \  
pip install requests-cache && \  
pip install babelfish && \  
pip install 'guessit<2' && \  
pip install 'subliminal<2' && \  
pip install stevedore==1.19.1 && \  
pip install python-dateutil && \  
pip install qtfaststart && \  
git clone https://github.com/mdhiggins/sickbeard_mp4_automator.git
/sickbeard_mp4_automator/ && \  
touch /sickbeard_mp4_automator/info.log && \  
cp /sickbeard_mp4_automator/autoProcess.ini.sample
/sickbeard_mp4_automator/autoProcess.ini && \  
chmod a+rwx -R /sickbeard_mp4_automator && \  
ln -s /downloads /data

