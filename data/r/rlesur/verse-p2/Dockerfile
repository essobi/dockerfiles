FROM rocker/verse:3.4.3  
  
## remove pandoc symlinks and install pandoc 2  
RUN rm /usr/local/bin/pandoc \  
&& rm /usr/local/bin/pandoc-citeproc \  
&& wget -O pandoc-2.1.1-1-amd64.deb
https://github.com/jgm/pandoc/releases/download/2.1.1/pandoc-2.1.1-1-amd64.deb
\  
&& dpkg -i pandoc-2.1.1-1-amd64.deb \  
&& rm pandoc-2.1.1-1-amd64.deb  
  

