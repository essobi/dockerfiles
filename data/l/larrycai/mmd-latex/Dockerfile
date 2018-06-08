FROM ubuntu:trusty  
  
MAINTAINER Larry Cai <larry.caiyu@gmail.com>  
  
RUN apt-get update && apt-get install -y texlive-xetex texlive-latex-
recommended texlive-latex-extra \  
latex-cjk-chinese fonts-arphic-gbsn00lp fonts-wqy-microhei fonts-wqy-zenhei
texlive-fonts-recommended \  
libglib2.0-dev git make cmake g++ \  
&& git clone git://github.com/fletcher/MultiMarkdown-5.git \  
&& cd MultiMarkdown-5 \  
&& ./update_git_modules \  
&& ./link_git_modules \  
&& make && cd build && make \  
&& cp multimarkdown /bin \  
&& cd / && rm -rf MultiMarkdown-5 \  
&& apt-get remove \--purge -y g++ cmake make git \  
&& rm -rf /var/lib/apt/lists/*  

