FROM nvidia/cuda:runtime  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y cmake libboost-all-dev python python-numpy default-jdk \  
zlib1g-dev libsdl2-dev libjpeg-dev nasm tar libbz2-dev \  
libgtk2.0-dev libfluidsynth-dev libgme-dev \  
libopenal-dev timidity \  
wget unzip git \  
fluid-soundfont-gs  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV DOOMWADDIR /vizdoom/scenarios  
  
WORKDIR /vizdoom  
  
RUN git clone \--depth 1 https://github.com/Marqt/ViZDoom .  
RUN cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_PYTHON=ON -DBUILD_JAVA=ON  
RUN make  
  
ENTRYPOINT [ "/vizdoom/bin/vizdoom" ]  

