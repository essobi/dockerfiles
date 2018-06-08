FROM linuxserver/sonarr  
  
# Add sources  
RUN sed -i -- 's/#deb-src/deb-src/g' /etc/apt/sources.list && sed -i -- 's/#
deb-src/deb-src/g' /etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get dist-upgrade -y  
RUN apt-get install -y libav-tools  
RUN apt-get install -y libavcodec-extra  
RUN apt-get install -y ffmpeg  
RUN apt-get install -y git  
RUN apt-get install -y python-pip  
RUN apt-get install -y openssl  
RUN apt-get install -y python-dev  
RUN apt-get install -y libffi-dev  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y libxml2-dev  
RUN apt-get install -y libxslt1-dev  
RUN apt-get install -y zlib1g-dev  
  
RUN apt-get install -y libfdk-aac-dev  
  
RUN \  
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
git clone git://github.com/mdhiggins/sickbeard_mp4_automator.git
/sickbeard_mp4_automator/ && \  
touch /sickbeard_mp4_automator/info.log && \  
chmod a+rwx -R /sickbeard_mp4_automator && \  
ln -s /downloads /data && \  
ln -s /config_mp4_automator/autoProcess.ini
/sickbeard_mp4_automator/autoProcess.ini && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
COPY manual_file.sh /sickbeard_mp4_automator/manual_file.sh  
  
COPY manual_folder.sh /sickbeard_mp4_automator/manual_folder.sh  
#RUN /bin/sh build_ffmpeg.sh  
VOLUME /config_mp4_automator  

