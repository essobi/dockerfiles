FROM insighttoolkit/itksoftwareguide-base  
MAINTAINER Matt McCormick <matt.mccormick@kitware.com>  
  
USER root  
RUN mkdir -p /usr/local/share/texmf/tex/latex/tex4ht  
COPY appendix.4ht /usr/local/share/texmf/tex/latex/tex4ht/  
RUN texhash  
USER itk  
  
RUN mkdir /home/itk/bin/ITKSoftwareGuide  
VOLUME ["/home/itk/bin/ITKSoftwareGuide"]  
WORKDIR /home/itk/bin/ITKSoftwareGuide  
ADD cmd.sh /tmp/cmd.sh  
CMD /tmp/cmd.sh  

