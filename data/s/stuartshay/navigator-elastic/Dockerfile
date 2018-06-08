############################################################  
# Dockerfile to run and restore mongo dump files  
# Based on mongo 3.2.3 Image  
############################################################  
  
FROM mongo:3.2.3  
  
RUN apt-get update && apt-get install -y \  
git \  
python \  
unzip \  
vim \  
wget \  
zip \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD python_libs.txt /python_libs.txt  
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
RUN pip install -r python_libs.txt  
  
ADD startup.sh /startup.sh  
ADD configure.sh /configure.sh  
ADD dbloader.py /dbloader.py  
ADD db.yml /db.yml  
ADD es_mapping.json /es_mapping.json  
  
RUN chmod a+x /startup.sh  
  
CMD ["/startup.sh"]  

