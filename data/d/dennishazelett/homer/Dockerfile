FROM ubuntu:14.04  
MAINTAINER Dennis Hazelett "dennis.hazelett@csmc.edu"  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN apt-get install -y zip unzip git wget ghostscript build-essential
zlib1g-dev libssl-dev libpng12-dev libmysqlclient-dev samtools  
  
RUN useradd -m user1  
  
## download and install HOMER software  
##  
WORKDIR /home/user1  
  
RUN wget http://weblogo.berkeley.edu/release/weblogo.2.8.2.tar.gz \  
&& tar xvfz weblogo.2.8.2.tar.gz \  
&& rm *.gz  
  
RUN git archive --format=zip -9 --remote=git://genome-
source.cse.ucsc.edu/kent.git beta src/userApps > userApps.zip \  
&& unzip userApps.zip \  
&& mv src/userApps . \  
&& rmdir src \  
&& rm userApps.zip  
  
WORKDIR /home/user1/userApps  
  
RUN make fetchSource \  
&& make \  
&& rsync -a -P /home/user1/userApps/bin/ /usr/local/bin/kentUtils/  
  
WORKDIR /home/user1/  
  
RUN git clone https://bitbucket.org/dennishazelett/homer \  
&& cd /home/user1/homer \  
&& mv .inputrc .. \  
&& rm Dockerfile contributors.txt .bash_profile \  
&& PATH=$PATH:/home/user1/blat/:/home/user1/weblogo/ \  
&& wget http://homer.salk.edu/homer/configureHomer.pl \  
&& perl configureHomer.pl -install homer  
  
RUN echo "PATH=$PATH:/home/user1/weblogo/:/home/user1/homer/bin/" >> .bashrc  
  
RUN chown -R user1:staff /home/user1  

