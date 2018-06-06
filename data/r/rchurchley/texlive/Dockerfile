FROM rchurchley/texlive:latest  
  
# Download Fira fonts, install them, and rebuild font caches.  
# Commands need to be run in bash (instead of sh) for globstar **/*.otf
pattern.  
RUN /bin/bash -c "apt-get update \  
&& apt-get install -y make unzip fontconfig libfontconfig \  
&& shopt -s globstar \  
&& cd /tmp \  
&& wget https://carrois.com/downloads/Fira/Fira_Sans_4_2.zip \  
&& wget https://carrois.com/downloads/Fira/Fira_Code_3_2.zip \  
&& wget https://carrois.com/downloads/Fira/Fira_Mono_3_2.zip \  
&& unzip Fira_Sans_4_2.zip \  
&& unzip Fira_Code_3_2.zip \  
&& unzip Fira_Mono_3_2.zip \  
&& cp Fira_*/**/*.otf /usr/local/share/fonts/ \  
&& fc-cache -fv \  
&& rm -R /tmp/*"  
  
# Default to compiling all .tex files in /data with XeLaTeX  
CMD ["latexmk", "-xelatex"]

