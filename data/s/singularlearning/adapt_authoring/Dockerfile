FROM node:6  
ENV ADAPT_VER=0.4.1  
ENV ADAPT_PORT=5000  
ENV ADAPT_SERVERNAME=localhost  
ENV ADAPT_DBHOST=adaptdb  
ENV ADAPT_DBNAME=adaptdatabase  
ENV ADAPT_DBPORT=27017  
ENV ADAPT_DATAROOT=data  
ENV ADAPT_SECRET=your-secret  
ENV ADAPT_SMTPSERVICE=serversmtp  
ENV ADAPT_SMTPUSERNAME=user  
ENV ADAPT_SMTPPASSWORD=passwd  
ENV ADAPT_FROMADDRESS=from@example.com  
ENV ADAPT_NAME=AD  
ENV ADAPT_DISPLAYNAME="SINGULAR LEARNING"  
ENV ADAPT_USEREMAIL=ADMIN  
ENV ADAPT_USERPASSWORD=ADMIN  
  
LABEL AUTHOR="Singular Learning"  
  
RUN apt-get update && apt-get install -y apt-utils  
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y --force-yes deb-multimedia-keyring  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
libssl-dev \  
xdg-utils  
  
# install ffmpeg  
RUN apt-get install -y libmp3lame0 libavdevice56 libx264-146 libvorbis0a
libtheora0 libspeex1 libfaac0 libopenjpeg5  
RUN apt-get install -y build-essential libmp3lame-dev libvorbis-dev libtheora-
dev libspeex-dev yasm pkg-config libfaac-dev libopenjpeg-dev libx264-dev  
RUN mkdir software && \  
cd software && \  
wget http://ffmpeg.org/releases/ffmpeg-3.4.2.tar.bz2 && \  
cd .. && \  
mkdir src && \  
cd src && \  
tar xvjf ../software/ffmpeg-3.4.2.tar.bz2 && \  
cd ffmpeg-3.4.2 &&\  
# ./configure --enable-gpl --enable-postproc --enable-swscale --enable-
avfilter --enable-libmp3lame --enable-libvorbis --enable-libtheora --enable-
libx264 --enable-libspeex --enable-shared --enable-pthreads --enable-
libopenjpeg --enable-libfaac --enable-nonfree && \  
./configure --enable-gpl --enable-postproc --enable-swscale --enable-avfilter
--enable-libmp3lame --enable-libvorbis --enable-libtheora --enable-libx264
--enable-libspeex --enable-shared --enable-pthreads --enable-libopenjpeg
--enable-nonfree && \  
make && make install && \  
/sbin/ldconfig && \  
cd / && \  
rm -rf src software  
  
RUN apt-get remove --purge -y build-essential libmp3lame-dev libvorbis-dev
libtheora-dev libspeex-dev yasm pkg-config libfaac-dev libopenjpeg-dev
libx264-dev  
RUN apt-get autoremove --purge -y  
  
RUN rm -rf /var/lib/apt/lists/*  
# global npm dependencies  
RUN npm install -g grunt-cli  
  
COPY install.sh /tmp/install.sh  
RUN chmod 0700 /tmp/install.sh  
COPY temp-server.js /tmp/temp-server.js  
RUN chmod 0700 /tmp/temp-server.js  
  
CMD ["/tmp/install.sh"]  
  
EXPOSE 5000  

