FROM phusion/baseimage:0.9.15  
ENV DEBIAN_FRONTEND noninteractive  
  
##java 8  
RUN \  
echo "===> add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
\  
\  
echo "===> install Java" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default && \  
\  
\  
echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
#####  
  
###create user  
RUN useradd -ms /bin/bash user  
###  
  
###install kamaki  
#RUN apt-get update -y && apt-get install software-properties-common -y &&
apt-get install python-software-properties -y  
#RUN apt-get update -y && add-apt-repository ppa:grnet/synnefo -y && apt-get
update -y && apt-get install kamaki -y  
### kamaki  
  
###install various  
RUN apt-get update -y && apt-get install nano dstat sysstat screen bash-
completion sshpass autossh sysbench git unzip wget build-essential -y  
#hmmer bioperl  
###  
  
##setup openssh hpn  
RUN add-apt-repository ppa:yoda-jazz-kc/hpn-ssh -y && \  
apt-get update && apt-get -y upgrade --force-yes && apt-get install -y
openssh-server && \  
mkdir -p /var/run/sshd && \  
echo "HPNDisabled no" >> /etc/ssh/sshd_config && \  
echo "TcpRcvBufPoll yes" >> /etc/ssh/sshd_config && \  
echo "HPNBufferSize 8192" >> /etc/ssh/sshd_config && \  
echo "NoneEnabled yes" >> /etc/ssh/sshd_config  
##  
  
  
WORKDIR /home/user  
  
### install pfam  
#RUN mkdir -p pfamAhmmDatabase && cd ./pfamAhmmDatabase && \  
#wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.dat.gz
&& \  
#gunzip *.gz && \  
#wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz  
###&& gunzip *.gz && hmmpress Pfam-A.hmm && rm Pfam-A.hmm  
##  
  
##setup PFAM environment  
#RUN apt-get update -y && apt-get install build-essential -y  
#RUN apt-get update -y && apt-get install bioperl -y  
#RUN export PERL_MM_USE_DEFAULT=1 && cpan Moose && echo 'export
PERL5LIB=/home/user/PfamScan:$PATH' >> /root/.bashrc  
##  
  
###install R  
RUN echo 'deb http://cran.rstudio.com/bin/linux/ubuntu trusty/' >>
/etc/apt/sources.list && gpg --keyserver keyserver.ubuntu.com --recv-key
E084DAB9 && gpg -a --export E084DAB9 | sudo apt-key add - && \  
apt-get update -y && apt-get upgrade -y && apt-get install libopenblas-base -y
&& \  
apt-get update -y && apt-get install r-base r-base-dev -y && \  
R -e "install.packages('dplyr', repos = 'http://cran.rstudio.com/')" && \  
R -e "install.packages('gplots', repos = 'http://cran.rstudio.com/')" && \  
R -e "install.packages('RColorBrewer', repos = 'http://cran.rstudio.com/')" &&
\  
R -e "install.packages('amap', repos = 'http://cran.rstudio.com/')"  
  
##git clone hermes components  
RUN git clone https://github.com/akintsakis/HermesComponents.git && mv
./HermesComponents ./Hermes  
  
####################finalized  
  
  
###setup ssh keys etc //deactivated, will take place locally  
#RUN rm -f /etc/service/sshd/down  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
#RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
#ADD id_thk.pub /tmp/id_thk.pub  
#ADD id_thk /root/.ssh/identity  
  
#RUN cat /tmp/id_thk.pub >> /root/.ssh/authorized_keys && rm -f
/tmp/id_thk.pub  
#RUN echo 'Host *' >> /root/.ssh/config  
#RUN echo 'StrictHostKeyChecking no' >> /root/.ssh/config  
#RUN echo 'IdentityFile /root/.ssh/identity' >> /root/.ssh/config  
###  

