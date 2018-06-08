FROM python:2  
MAINTAINER Paul Liljenberg <liljenberg.paul@gmail.com>  
  
RUN git clone https://bitbucket.org/LaNMaSteR53/recon-ng.git \  
&& cd recon-ng \  
&& pip install -r REQUIREMENTS  
  
WORKDIR /recon-ng  
  
ENTRYPOINT ["./recon-ng"]  

