FROM ubuntu:14.04  
MAINTAINER Kyle Mathews "mathews.kyle@gmail.com" & Mark Milstein
"mark@epiloque.com"  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty main universe" >>
/etc/apt/sources.list  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y git wget lsb-release sudo time unzip fontconfig  
  
# Install all Google Web Fonts  
RUN mkdir fonts  
RUN wget https://github.com/google/fonts/archive/master.zip -O
fonts/master.zip  
RUN cd fonts; unzip master.zip  
RUN mkdir -p /usr/share/fonts/truetype/google-fonts/  
RUN find $PWD/fonts/ -name "*.ttf" -exec install -m644 {}
/usr/share/fonts/truetype/google-fonts/ \; || return 1  
RUN fc-cache -f -v  
RUN rm -rf fonts  
  
# Install the texlive-xetex package which includes the Xelatex executable.  
RUN git clone https://github.com/scottkosty/install-tl-ubuntu.git && \  
cd install-tl-ubuntu && \  
./install-tl-ubuntu  
  
RUN PATH="/opt/texbin:$PATH" && \  
tlmgr update --self && \  
tlmgr update --all  
  
RUN apt-get clean && rm -rf /install-tl-ubuntu /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  

