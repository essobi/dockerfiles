  
FROM nlpbox/nlpbox-base:16.04  
RUN apt-get update -y && apt-get upgrade -y && \  
apt-get install -y python3 python3-pip && \  
pip3 install six  
  
WORKDIR /opt  
RUN git clone https://github.com/EducationalTestingService/python-zpar  
  
WORKDIR /opt/python-zpar  
RUN python3 setup.py install  
  
WORKDIR /opt/zpar-0.7/models  
RUN wget -O english.zip
http://sourceforge.net/projects/zpar/files/0.7/english.zip/download && \  
dtrx english.zip && rm english.zip  
  
EXPOSE 8859  
# load all english models (tagger, constituency parser, dependency parser)  
#CMD zpar_server --modeldir /opt/zpar-0.7/models/english --models tagger
parser depparser  
# only load the english constituency parser model  
CMD zpar_server --modeldir /opt/zpar-0.7/models/english --models parser  

