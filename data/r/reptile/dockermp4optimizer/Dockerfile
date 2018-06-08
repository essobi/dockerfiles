FROM phusion/baseimage:0.9.22  
MAINTAINER Filechaser <>  
#Zusätzliche Repos  
RUN add-apt-repository ppa:jonathonf/ffmpeg-3  
  
#Basiseinrichtung des Testservers  
RUN apt-get update && apt-get install -qy \  
vim \  
git \  
wget \  
mc \  
curl \  
zsh \  
build-essential \  
cmake \  
python-dev \  
htop \  
locales  
  
#Locales  
RUN locale-gen "en_US.UTF-8"  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get install -qy \  
python2.7 \  
python-pip \  
python-dev \  
libffi-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
libjpeg8-dev \  
zlib1g-dev \  
ffmpeg  
  
#Software für mp4automator  
RUN pip install -U pip setuptools  
RUN pip install requests  
RUN pip install requests[security]  
RUN pip install requests-cache  
RUN pip install babelfish  
RUN pip install "guessit<2"  
RUN pip install "subliminal<2"  
RUN pip uninstall stevedore --y  
RUN pip install stevedore==1.19.1  
RUN pip install python-dateutil  
RUN pip install deluge-client  
RUN pip install qtfaststart  
  
#RUN mkdir /mp4converter  
RUN git clone https://github.com/Filechaser/sickbeard_mp4_automator
/mp4converter/  
RUN cp /mp4converter/autoProcess.sample-Filechaser
/mp4converter/autoProcess.ini  
#Non Root User 1000 anlegen  
RUN chown -R 1000:1000 /mp4converter  
RUN adduser --system --home /mp4converter --uid 1000 --group --shell /bin/bash
dockermanualuser  
RUN chown -R 1000:1000 /mp4converter  
RUN apt-get update && apt-get install -qy \  
libx264-dev  
RUN mkdir /filestoconvert  
RUN chown -R 1000:1000 /filestoconvert  
COPY startconvertion.sh /startconvertion.sh  
RUN chmod +x /startconvertion.sh && chmod 700 /startconvertion.sh  
VOLUME ["/static-mp4converter/","/mp4converter/"]  
  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
  
#Clean Installdirs  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
CMD ["/sbin/my_init"]  

