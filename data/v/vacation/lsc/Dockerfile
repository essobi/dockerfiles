from vacation/splicemap:3.3.7  
# Starting from the splicemap build  
ENV REPO https://github.com/jason-weirather/LSC.git  
RUN git clone $REPO /Source/LSC \  
&& cd /Source/LSC  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
python-pip \  
libz-dev  
  
ENV PATH="/Source/LSC/bin:${PATH}"  
ENV REPO https://github.com/BenLangmead/bowtie2.git  
RUN git clone $REPO /Source/Bowtie2 \  
&& cd /Source/Bowtie2 \  
&& git checkout c614bc1560f9202f5cdbc845e20e9ce804ec58cd \  
&& make \  
&& cp bowtie2* /usr/local/bin/ \  
&& rm -r /Source/Bowtie2  
  
VOLUME /temp  
VOLUME /output  
VOLUME /home  
ENV HOME /home  
WORKDIR /home  

