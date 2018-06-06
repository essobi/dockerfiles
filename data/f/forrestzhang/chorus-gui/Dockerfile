FROM dorowu/ubuntu-desktop-lxde-vnc  
  
MAINTAINER Tao Zhang "forrestzhang1982@gmail.com"  
RUN apt-get update && apt-get install -y cython3 build-essential \  
zlib1g-dev \  
zlibc \  
git \  
libboost-dev \  
autoconf \  
libncursesw5-dev \  
libncurses5 \  
ncurses-dev \  
libboost-thread-dev \  
python3-pip \  
samtools \  
unzip \  
python \  
curl \  
wget \  
python3-pyqt5 \  
libfreetype6-dev \  
libxft-dev \  
python3-matplotlib  
  
RUN apt-get remove -y python3-matplotlib  
  
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
RUN mkdir /opt/software  
WORKDIR /opt/software  
ADD
https://github.com/gmarcais/Jellyfish/releases/download/v2.2.3/jellyfish-2.2.3.tar.gz
/opt/software/  
RUN tar zxvf jellyfish-2.2.3.tar.gz && mv jellyfish-2.2.3 jellyfish && cd
jellyfish && ./configure && make && make install  
  
#WORKDIR /opt/software  
ADD https://github.com/forrestzhang/primer3-py/archive/unicode.zip
/opt/software/  
RUN unzip unicode.zip && cd primer3-py-unicode && python3.4 setup.py install  
  
RUN git clone https://github.com/forrestzhang/Chorus.git  
#WORKDIR /opt/software  
RUN git clone https://github.com/lh3/bwa.git && cd bwa && make  
  
RUN pip3 install numpy pyfasta matplotlib pandas  
  
#RUN mkdir Chorus  
# RUN mkdir -p Chorus/Choruslib  
# ADD Chorus.py Chorus/  
# ADD Choruslib/* Chorus/Choruslib/  
RUN mkdir -p /home/ubuntu/Desktop  
RUN echo "python3 /opt/software/Chorus/ChorusGUI.py" >
/home/ubuntu/Desktop/ChorusGUI.sh  
RUN echo "python3 /opt/software/Chorus/ChorusPBselect.py" >
/home/ubuntu/Desktop/ChorusPBselect.sh  
RUN chmod +x /home/ubuntu/Desktop/ChorusGUI.sh
/home/ubuntu/Desktop/ChorusPBselect.sh  
ENV PATH /opt/software/bwa:/opt/software/jellyfish/bin:$PATH  
  
EXPOSE 6080  
WORKDIR /opt/software/Chorus  
VOLUME /home/ubuntu/Data  
ENTRYPOINT ["/startup.sh"]  

