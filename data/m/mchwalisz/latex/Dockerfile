FROM ubuntu:latest  
MAINTAINER Mikołaj Chwalisz <m.chwaliszATgmail.com>  
  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:jonathonf/texlive-2017  
RUN apt-get update  
RUN apt-get install -y \  
make \  
graphviz \  
default-jre \  
icc-profiles \  
wget  
RUN apt-get install -y \  
texlive-full \  
texlive-latex-extra \  
biber \  
latexmk  
RUN rm -rf /var/lib/apt/lists/*  
  
ENV PLANTUMLDIR /usr/share/plantuml  
RUN mkdir $PLANTUMLDIR  
RUN wget -O $PLANTUMLDIR/plantuml.jar
http://sourceforge.net/projects/plantuml/files/plantuml.jar/download  
RUN wget -O $PLANTUMLDIR/batik-bin-1.9.tar.gz
http://apache.mirror.digionline.de/xmlgraphics/batik/binaries/batik-
bin-1.9.tar.gz  
RUN tar -x -C $PLANTUMLDIR -f $PLANTUMLDIR/batik-bin-1.9.tar.gz  
RUN mv $PLANTUMLDIR/batik-1.9/*.jar $PLANTUMLDIR/  
RUN wget -O $PLANTUMLDIR/fop-2.2-bin.tar.gz
http://apache.mirror.digionline.de/xmlgraphics/fop/binaries/fop-2.2-bin.tar.gz  
RUN tar -x -C $PLANTUMLDIR -f $PLANTUMLDIR/fop-2.2-bin.tar.gz  
RUN mv $PLANTUMLDIR/fop-2.2/fop/build/*.jar $PLANTUMLDIR/  
RUN mv $PLANTUMLDIR/fop-2.2/fop/lib/*.jar $PLANTUMLDIR/  
  
ADD plantuml /usr/bin/plantuml  
ADD latexmkrc /root/.latexmkrc  
  
WORKDIR /doc  
VOLUME /doc  
CMD ["latexmk"]  

