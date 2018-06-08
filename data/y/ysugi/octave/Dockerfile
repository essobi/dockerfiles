FROM debian  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y sudo make python python-dev python3 python3-dev \  
htop tmux octave gnuplot epstool transfig less \  
&& apt-get clean  
  
RUN useradd imrc -m -b /home \  
&& echo 'imrc:imrc' | chpasswd \  
&& echo 'imrc ALL = NOPASSWD : ALL' >>/etc/sudoers.d/imrc  
  
USER imrc  
ENV HOME /home/imrc  
RUN sudo chown imrc:imrc -R $HOME  
WORKDIR $HOME  
  
CMD /bin/bash  

