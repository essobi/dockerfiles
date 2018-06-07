FROM ubuntu:12.04  
MAINTAINER Hoseog Lee <hoseog@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SIRIUS_HOME /opt/sirius  
RUN export SIRIUS_HOME=$SIRIUS_HOME  
  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise main restricted
universe multiverse" >> /etc/apt/sources.list;\  
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-updates main
restricted universe multiverse" >> /etc/apt/sources.list;\  
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-backports main
restricted universe multiverse" >> /etc/apt/sources.list;\  
echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-security main
restricted universe multiverse" >> /etc/apt/sources.list  
  
RUN apt-get update;\  
apt-get install -y \  
apt-utils \  
git wget unzip \  
libfaac-dev vim sudo aptitude \  
python-pip python-dev subversion\  
build-essential  
RUN pip install --upgrade pip  
RUN pip install --upgrade virtualenv  
RUN pip install pickledb  
RUN aptitude install -y sox  
  
#Download sirius source  
RUN git clone https://github.com/jhauswald/sirius.git $SIRIUS_HOME  
  
#Setting up sirius  
WORKDIR $SIRIUS_HOME/sirius-application  
RUN ./get-dependencies.sh  
RUN ./get-kaldi.sh  
RUN ./get-opencv.sh  
#RUN ./compile-sirius-servers.sh  
#Automatic Speech Recognition(ASR)  
#RUN $SIRIUS_HOME/sirius-application/run-scripts/start-asr-server.sh  
#Image Matching(IMM)  
#RUN $SIRIUS_HOME/sirius-application/image-matching/make-db.py landmarks
$SIRIUS_HOME/sirius-application/image-matching/matching/landmarks/db/  
#RUN $SIRIUS_HOME/sirius-application/image-matching/start-imm-server.sh  
#Question-Answering System(QA)  

