#docker run -ti --rm --name tts -p 8000:80 -v
/var/docker/tts/static:/var/static -v /var/docker/tts/media:/media -v
/var/docker/tts/conf:/conf -v /var/docker/tts/data:/data bm0/tts  
FROM ubuntu:17.10  
MAINTAINER bm0 <bm0@soft-way.biz>  
  
EXPOSE 80  
VOLUME /media  
VOLUME /data  
VOLUME /conf  
VOLUME /static  
  
# install dependencies  
RUN apt-get update &&\  
apt-get install -y\  
python3-pip\  
git\  
gcc\  
nginx\  
scons\  
libao4\  
locales\  
libao-dev\  
supervisor\  
pkg-config  
  
# Setting the locale  
RUN locale-gen ru_RU.UTF-8  
ENV LANG ru_RU.UTF-8  
ENV LANGUAGE ru_RU:ru  
ENV LC_ALL ru_RU.UTF-8  
# build RHVoice  
RUN git clone https://github.com/Olga-Yakovleva/RHVoice.git /tmp/RHVoice  
WORKDIR /tmp/RHVoice  
RUN scons && scons install && ldconfig  
  
# cleanup  
RUN rm -rf /var/lib/{apt,dpkg,cache,log} &&\  
rm -rf /opt/RHVoice &&\  
apt-get clean auteclean &&\  
apt-get autoremove -y &&\  
apt-get purge -y\  
git\  
gcc\  
scons\  
libao-dev\  
pkg-config  
  
# copying source  
COPY . /opt/tts  
WORKDIR /opt/tts  
RUN cp conf/supervisor.conf /etc/supervisor/conf.d/tts.conf &&\  
cp conf/nginx.conf /etc/nginx/sites-enabled/tts &&\  
cp conf/RHVoice.conf /usr/local/etc/RHVoice/RHVoice.conf  
  
# disable default Nginx site  
RUN rm /etc/nginx/sites-enabled/default  
RUN pip3 install -r requirements.txt  
  
CMD ./bootstrap.sh  

