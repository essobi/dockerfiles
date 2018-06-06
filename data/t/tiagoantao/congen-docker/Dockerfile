FROM continuumio/anaconda3  
MAINTAINER tiagoantao@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update; apt-get install -y emacs vim nano openssh-server lxde
vnc4server build-essential zlib1g-dev libgsl0-dev -y unzip tmux screen
firefox-esr net-tools xfce4-terminal; apt-get remove -y lxterminal; apt-get
clean  
  
RUN conda update --all; conda config --add channels r; conda config --add
channels bioconda;conda install -y bwa samtools picard vcftools plink2 stacks
r r-vegan r-devtools bioconductor-qvalue;  
  
RUN mkdir /var/run/sshd; ssh-keygen -A; sed -i 's/PermitRootLogin without-
password/PermitRootLogin yes/g' /etc/ssh/sshd_config; echo "root:congen17" |
chpasswd; echo PasswordAuthentication yes >> /etc/ssh/sshd_config;  
  
RUN mkdir /root/.vnc; echo congen17 > pass; echo congen17 >> pass; vncpasswd <
pass; rm pass  
COPY xstartup /root/.vnc  
RUN chmod a+x /root/.vnc/xstartup  
  
RUN git clone https://github.com/kanaka/noVNC.git  
COPY launch.sh /noVNC/utils  
WORKDIR /noVNC  
RUN cp vnc.html index.html  
WORKDIR /noVNC/utils  
RUN git clone https://github.com/kanaka/websockify  
WORKDIR /  
  
COPY prepare_negui.sh /  
RUN chmod a+x prepare_negui.sh; conda create -n python2 python=2;
./prepare_negui.sh; git clone https://github.com/popgengui/negui.git  
WORKDIR /negui  
RUN git checkout origin/develop; git checkout -b dev  
WORKDIR /  
  
RUN ln -s /bin/tar /bin/gtar  
RUN echo
"source('https://bioconductor.org/biocLite.R')\nbiocLite('LEA')\ninstall.packages('RepeatABEL',
repos='http://cran.us.r-project.org')\ndevtools::install_github('ngthomas/microhaplot',
build_vignettes = TRUE)" > R.inst  
RUN R --no-save < R.inst  
  
RUN git clone https://github.com/arunsethuraman/ima2p.git  
WORKDIR /ima2p  
RUN chmod a+x configure; ./configure; make install  
WORKDIR /  
  
RUN wget http://popgen.net/ms.tar.gz; tar zxf ms.tar.gz  
WORKDIR msdir  
RUN gcc -O3 -o ms ms.c streec.c rand1.c -lm; cp ms /usr/bin  
WORKDIR /  
  
RUN wget https://bio.cst.temple.edu/~hey/downloads/IMfig.py  
  
RUN mkdir /data  
VOLUME /data  
  
COPY run.sh run.sh  
RUN chmod a+x run.sh  
  
EXPOSE 22 5901 6080  
CMD ./run.sh  

