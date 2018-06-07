# Set base image  
FROM fedora:latest  
  
# Metadata  
LABEL maintainer="OP5"  
  
# Build Image  
#RUN echo "**** Update All Packages ****" && \  
# dnf -y update && \  
# echo "**** Clean cache ****" && \  
# dnf clean all && \  
# echo "**** Install required packages ****" && \  
# dnf -y install pandoc pandoc-pdf texlive-ulem texlive-datetime texlive-
isodate texlive-tocloft texlive-upquote texlive-substr && \  
# echo "**** Clean cache ****" && \  
# dnf clean all  
RUN dnf -y install pandoc pandoc-pdf texlive-ulem texlive-datetime texlive-
isodate texlive-tocloft texlive-upquote texlive-substr  
  
# Volumes  
VOLUME /docs  
  
ADD entrypoint.sh /  
  
RUN chmod a+x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

