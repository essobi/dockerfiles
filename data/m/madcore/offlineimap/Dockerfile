FROM python:2.7  
ENV PATH_BASE /var/offlineimap  
ENV PATH_APP $PATH_BASE/app  
ENV PATH_DATA /opt/offlineimap  
  
RUN apt-get update  
RUN apt-get install -y git  
  
RUN mkdir -p $PATH_APP  
RUN mkdir $PATH_DATA  
  
RUN git clone -b gmail-oauth https://github.com/styk-tv/offlineimap.git
$PATH_APP  
RUN cd $PATH_APP && python setup.py install  
  
ADD utf7.py $PATH_BASE/utf7.py  
ADD run.sh $PATH_BASE/run.sh  
  
CMD /bin/bash -c $PATH_BASE/run.sh  

