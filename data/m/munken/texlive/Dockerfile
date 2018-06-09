FROM sumdoc/texlive-2017  
  
RUN apt-get -y update && apt-get -y install \--no-install-recommends \  
ghostscript git\  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \  
&& python get-pip.py  
RUN git clone https://gitlab.com/git-latexdiff/git-latexdiff.git \  
&& cp git-latexdiff/git-latexdiff /usr/bin/ \  
&& rm -rf git-latexdiff  
  

