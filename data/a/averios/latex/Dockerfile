FROM ubuntu:14.04  
MAINTAINER I Putu Pradnyana <saintrx@gmail.com>  
RUN echo "deb http://us-west-2.ec2.archive.ubuntu.com/ubuntu/ trusty
multiverse" >> /etc/apt/sources.list.d/multiverse.list \  
&& echo "deb http://us-west-2.ec2.archive.ubuntu.com/ubuntu/ trusty-updates
multiverse" >> /etc/apt/sources.list.d/multiverse.list \  
&& echo "deb http://us-west-2.ec2.archive.ubuntu.com/ubuntu/ trusty-backports
main restricted universe multiverse" >>
/etc/apt/sources.list.d/multiverse.list  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | debconf-set-selections  
RUN apt-get update && apt-get install -y texlive \  
texlive-xetex \  
texlive-lang-other \  
python \  
python-pip \  
xzdec \  
wget \  
curl \  
git \  
texlive-science \  
&& apt-get --reinstall install -y ttf-mscorefonts-installer  
RUN pip install pygments  
RUN tlmgr init-usertree && tlmgr install minted \  
lineno \  
xcolor \  
tocbibind \  
algorithmicx \  
algorithm2e  

