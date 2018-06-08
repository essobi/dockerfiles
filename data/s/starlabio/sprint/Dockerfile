FROM phusion/baseimage:0.9.19  
RUN apt-get --quiet --yes update && \  
apt-get --quiet --yes install git-core python2.7 python-dev python-pip curl  
  
RUN pip install gitpython jsonpickle bleach  
  
RUN mkdir -p /opt/sprint  
WORKDIR /opt/  
  
RUN git clone https://github.com/mrozekma/Sprint sprint  
  
RUN git clone https://github.com/mrozekma/Rorn.git sprint/rorn  
RUN git clone https://github.com/mrozekma/Stasis.git sprint/stasis  
  
RUN groupadd -r sprint && useradd -r -g sprint sprint  
RUN chown -R sprint:sprint /opt/sprint/  
  
USER sprint  
RUN mkdir /opt/sprint/db && chown -R sprint:sprint /opt/sprint/db  
EXPOSE 8081  
VOLUME ["/opt/sprint/db"]  
  
WORKDIR /opt/sprint  
  
CMD ["python2.7", "sprint.py"]  

