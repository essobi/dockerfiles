FROM ubuntu:17.10  
ENV BEETSDIR /etc/beets/  
  
RUN apt-get -y update && apt-get install -y \  
locales \  
python3-pip \  
bs1770gain \  
libchromaprint-tools \  
ffmpeg \  
curl  
  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LANGUAGE en_GB:en  
ENV LC_ALL en_GB.UTF-8  
RUN pip3 install \  
beets[fetchart,lastgenre,chroma,web]==1.4.6 \  
beets-copyartifacts \  
flask  
  
# Manually add the latest version of the Copy Artifacts plugin for Python 3
compatibility.  
RUN curl https://raw.githubusercontent.com/sbarakat/beets-
copyartifacts/master/beetsplug/copyartifacts.py --create-dirs -o
/usr/local/lib/python3.6/dist-packages/beetsplug/copyartifacts.py  
  
COPY config.yaml /etc/beets/config.yaml  
  
EXPOSE 8337  
VOLUME /etc/beets /music /import /convert  
  
CMD beet web  

