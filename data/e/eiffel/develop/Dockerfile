FROM eiffel/eiffel:dev  
MAINTAINER Jocelyn Fiat  
  
ENV PATH
$PATH:$ISE_EIFFEL/studio/spec/$ISE_PLATFORM/bin:$ISE_EIFFEL/tools/spec/$ISE_PLATFORM/bin:$ISE_EIFFEL/library/gobo/spec/$ISE_PLATFORM/bin  
  
USER root  
RUN apt-get update && apt-get install -y \  
sudo \  
xterm tmux \  
mysql-client \  
subversion git-all tig \  
vim \  
&& sudo adduser eiffel sudo \  
&& echo "eiffel:eiffel" | chpasswd  
  
USER eiffel  
ENV HOME /home/eiffel  
ADD ./home/eiffel/.subversion /home/eiffel/.subversion  
  
RUN iron update  
  
WORKDIR /home/eiffel  
  
##################################  
# Custom EiffelStudio trunk dev. #  
##################################  
ENV EIFFEL_SRC /home/eiffel/trunk/Src  
ENV ISE_LIBRARY $EIFFEL_SRC  
  
RUN mkdir -p /home/eiffel/trunk \  
&& svn checkout https://svn.eiffel.com/eiffelstudio/trunk/Src
/home/eiffel/trunk/Src  
WORKDIR $EIFFEL_SRC  
RUN geant prepare  
  
WORKDIR /home/eiffel  

