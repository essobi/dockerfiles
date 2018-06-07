FROM ontouchstart/texlive-full  
  
# update  
RUN apt-get update  
RUN apt-get upgrade -y  
WORKDIR /root  
  
# download and unpack iclr style files  
ADD
http://www.iclr.cc/lib/exe/fetch.php?media=iclr2016:iclr2016_stylefiles_conference.zip
iclrstyle.zip  
RUN unzip iclrstyle.zip && mv iclr2016_stylefiles_conference/* . && rm -r
iclr2016_stylefiles_conference  
  
# make output a volume  
RUN mkdir out && mkdir aux  
VOLUME /root/out  
  
# paper name assumed to be "paper.tex", override this environment variable
otherwise  
ENV TEXFILE paper.tex  
  
# run command to produce pdf in output file, and watch for changes  
CMD latexmk -outdir=out -bibtex -pdf -pvc $TEXFILE  

