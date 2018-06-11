FROM centos:7  
MAINTAINER The U-TEST Team  
  
# add repo for last pandoc  
RUN echo -e "[puias]\nname=Puias
Computational\nbaseurl=http://springdale.math.ias.edu/data/puias/computational/7/x86_64/\ngpgcheck=0\nenabled=1"
>> /etc/yum.repos.d/puias-computational.repo  
# and install it  
RUN yum install -y pandoc  
  
# add filters for python  
RUN yum install -y wget && \  
wget https://github.com/jgm/pandocfilters/archive/1.4.2.tar.gz && \  
tar xzf 1.4.2.tar.gz && \  
cd pandocfilters-1.4.2 && \  
python setup.py install && \  
cd .. && \  
rm -rf pandocfilters-1.4.2  
  
# add tex-live for xelatex  
ADD texlive.profile .  
RUN yum install -y perl-Tk perl-Digest-MD5 && \  
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \  
mkdir -p install-tl && \  
tar xzf install-tl-unx.tar.gz -C install-tl \--strip-components=1 && \  
cd install-tl && \  
./install-tl -profile ../texlive.profile && \  
cd .. && \  
rm -rf install-tl  
ENV PATH="/usr/local/texlive/2017/bin/x86_64-linux/:${PATH}"  

