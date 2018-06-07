FROM python:2.7  
MAINTAINER Tale Toul <tale.toul@gmail.com>  
ENV USR pinton  
ENV AP /home/$USR/PrimeFactor/  
ENV PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages  
RUN apt-get -y update && apt install -y \  
python-gmpy2 \  
python-twisted  
RUN adduser --disabled-password --gecos "$USR" $USR && \  
echo "export PYTHONPATH='\$PYTHONPATH:/usr/lib/python2.7/dist-packages'" >>
/home/$USR/.bashrc  
USER $USR  
COPY *.py $AP  
WORKDIR $AP  
ENTRYPOINT ["./PrimeFactor.py"]  

