FROM unibaktr/mininet  
MAINTAINER Marcel Grossmann <whatever4711@gmail.com>  
LABEL architecture="amd64"  
  
RUN apt-get update \  
&& apt-get install -y \  
git \  
python2.7 \  
python-pip \  
python-tk  
  
WORKDIR /mininet  
RUN git clone https://github.com/mininet/mininet .  
ENTRYPOINT []  
CMD ["python","examples/miniedit.py"]  

