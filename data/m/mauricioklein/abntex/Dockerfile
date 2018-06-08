FROM ubuntu:latest  
MAINTAINER Mauricio Klein <mauricio.klein.msk@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
texlive-publishers \  
texlive-lang-portuguese \  
texlive-latex-extra \  
texlive-fonts-recommended \  
abntex \  
uuid-runtime  
  
ADD process.bash /root/  
RUN chmod +x /root/process.bash  
  
ENTRYPOINT /root/process.bash -  

