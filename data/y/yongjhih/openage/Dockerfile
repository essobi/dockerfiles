FROM ubuntu:15.04  
RUN apt-get update && apt-get install -y \  
cmake \  
libfreetype6-dev \  
python3-dev \  
libepoxy-dev \  
libsdl2-dev \  
ftgl-dev \  
alsa-base \  
alsa-utils \  
alsa-oss \  
libsdl2-image-dev \  
libopusfile-dev \  
libfontconfig1-dev \  
libharfbuzz-dev \  
opus-tools \  
python3-pil \  
python3-numpy \  
python3-pygments \  
python3-pip \  
g++ \  
git \  
vim  
  
RUN pip3 install cython  
RUN pip3 install pep8  
RUN pip3 install pylint  
  
RUN mkdir /app  
WORKDIR /app  
RUN git clone https://github.com/SFTtech/openage.git  
WORKDIR /app/openage  
RUN ./configure && make  
  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
mkdir -p /etc/sudoers.d && \  
chmod -R 0440 /etc/sudoers.d && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer && \  
chown ${uid}:${gid} -R /app/openage  
  
USER developer  
ENV HOME /home/developer  
ENV AGE2DIR /app/age2dir  
ENV LANG C.UTF-8  
CMD ./run  

