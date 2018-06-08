FROM vvakame/review  
  
MAINTAINER Yamamoto Yu  
  
RUN apt-get update && \  
apt-get install -y graphviz \  
fonts-ipafont \  
python-setuptools \  
python-imaging \  
python-reportlab && \  
apt-get clean  
  
RUN easy_install pip  
RUN pip install blockdiag seqdiag actdiag nwdiag  
  
RUN apt-get update && \  
apt-get install -y default-jre && \  
apt-get clean  
  
RUN mkdir /java && \  
curl -sL https://sourceforge.net/projects/plantuml/files/plantuml.jar \  
> /java/plantuml.jar  
  
RUN apt-get update && \  
apt-get install -y librsvg2-bin && \  
apt-get clean  
  
RUN mkdir /docs  
WORKDIR /docs  
  

