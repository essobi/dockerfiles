FROM ubuntu:18.04  
RUN apt update  
  
# for tex  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt install -y texlive-latex-extra texlive-fonts-recommended texlive-lang-
japanese fonts-lmodern  
  
# for review  
RUN apt install -y rbenv ruby-build ruby-dev  
RUN gem install review review-peg --no-rdoc --no-ri  
  
# for noto font  
RUN apt install -y fonts-noto-cjk fonts-noto-cjk-extra  
RUN apt install -y git  
RUN git clone https://github.com/vvakame/docker-review.git  
RUN mv docker-review/noto /usr/share/texlive/texmf-
dist/fonts/map/dvipdfmx/ptex-fontmaps/  
RUN rm -rf docker-review  
RUN mktexlsr && kanji-config-updmap-sys noto  
  
CMD ["/bin/bash"]  

