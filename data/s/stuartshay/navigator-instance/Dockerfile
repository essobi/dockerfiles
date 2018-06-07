############################################################  
# Dockerfile to run and restore mongo dump files  
# Based on mongo 3.4 Image  
############################################################  
  
FROM mongo:3.4  
  
RUN apt-get update && apt-get install -y \  
git \  
python \  
unzip \  
vim \  
wget \  
zip \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD python_libs.txt /python_libs.txt  
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
RUN pip install -r python_libs.txt  
  
  
# Scripts  
RUN mkdir -p /scripts  
COPY scripts /scripts  
RUN chmod +x -R /scripts  
  
  
ADD startup.sh /startup.sh  
ADD dbloader.py /dbloader.py  
ADD db.yml /db.yml  
  
RUN mkdir backup  
  
RUN chmod a+x /startup.sh  
EXPOSE 27017 28017  
  
VOLUME ["/backup"]  
CMD ["/startup.sh"]  

