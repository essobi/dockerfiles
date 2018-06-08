FROM k4zuki/pandocker-base  
  
MAINTAINER k4zuki  
  
ENV TZ JST-9  
WORKDIR /usr/local/bin  
RUN wget -c
https://github.com/tcnksm/ghr/releases/download/v0.5.4/ghr_v0.5.4_linux_amd64.zip
&& \  
unzip -e ghr_v0.5.4_linux_amd64.zip && rm ghr_v0.5.4_linux_amd64.zip  
  
RUN pip3 install git+https://github.com/K4zuki/wavedrompy.git \  
git+https://github.com/K4zuki/bitfieldpy.git \  
git+https://github.com/K4zuki/pandocker-filters.git \  
git+https://github.com/pandocker/removalnotes.git \  
git+https://github.com/pandocker/tex-landscape.git \  
git+https://github.com/pandocker/pandoc-blockdiag-filter.git  
  
WORKDIR /var  
ENV PANDOC_MISC_VERSION -b 0.0.28  
RUN git clone \--recursive --depth=1 $PANDOC_MISC_VERSION
https://github.com/K4zuki/pandoc_misc.git && \  
apt install -y --no-install-recommends texlive-pstricks  
  
WORKDIR /workdir  
  
VOLUME ["/workdir"]  
  
CMD ["bash"]  

