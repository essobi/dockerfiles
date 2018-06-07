FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y install \  
apt-utils \  
curl \  
fontconfig \  
git \  
gnuplot \  
libfontconfig1 \  
make \  
perl \  
sudo \  
vim \  
wget  
  
ADD texlive.profile.2015 /tmp/texlive.profile  
  
ADD http://mirror.physik-pool.tu-berlin.de/tex-
archive/systems/texlive/tlnet/install-tl-unx.tar.gz /tmp/install.tar.gz  
  
RUN mkdir /tmp/install-tl  
  
RUN tar -xi -f /tmp/install.tar.gz -C /tmp/install-tl/ --strip-components=1  
  
RUN ls -lah /tmp/install-tl  
  
# For the ./install-tl command you can specify the option --location <URL>. A
list of possbile mirrors can be found at  
# https://www.ctan.org/mirrors  
# You can also leave the option unset to use the auto-selection of the
closes/fastest mirror available  
RUN \  
/tmp/install-tl/install-tl \  
\--profile=/tmp/texlive.profile && \  
rm -rf /tmp/texlive* /tmp/install-tl*  
  
RUN tlmgr update --self && tlmgr update --all  
  
RUN groupadd -g 1000 latex && useradd -u 1000 -g latex latex  
USER latex  
ADD latexmkrc /home/latex/.latexmkrc  
  
WORKDIR /data  
ENTRYPOINT ["latexmk"]  
CMD ["-help"]  

