FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
texlive-full \  
make \  
git \  
wget \  
curl \  
fontconfig \  
texlive-fonts-extra \  
texlive-latex-extra \  
texlive-math-extra \  
latex-xcolor \  
texlive-xetex && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /docs  
WORKDIR /docs  
  
COPY main.sh /  
  
ENTRYPOINT ["/main.sh"]  
CMD ["default"]  
  

