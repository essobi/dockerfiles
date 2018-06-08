# required testing for findutils >= 4.5  
FROM debian:testing  
MAINTAINER Iskaron <mail@iskaron.de>  
  
RUN apt-get update && apt-get install -y wget bzip2 ghostscript openssh-client
git && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
  
ADD
http://download.linuxaudio.org/lilypond/binaries/linux-64/lilypond-2.18.2-1.linux-64.sh
./  
RUN chmod +x lilypond-2.18.2-1.linux-64.sh  
RUN ./lilypond-2.18.2-1.linux-64.sh --batch --prefix /root/stable  
RUN rm lilypond-2.18.2-1.linux-64.sh  
COPY lilyfy.sh /root/stable/bin  
  
ENV PATH /root/stable/bin:$PATH  
  

