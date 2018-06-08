FROM debian  
  
RUN apt-get update && \  
apt-get -y install texlive-full git curl  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN update-texmf && \  
texhash  
  
RUN useradd -md /texlive texlive  
  
USER texlive  
  
RUN mkdir -p /texlive/work  
RUN mkdir -p /texlive/texmf  
COPY libraries /texlive/texmf  
  
WORKDIR /texlive/work  

