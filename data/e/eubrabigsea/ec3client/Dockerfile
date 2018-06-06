FROM ubuntu  
RUN apt-get update  
RUN apt-get -y -q install git  
RUN git clone \--branch devel https://github.com/grycap/ec3  
RUN apt-get -y -q install python  
RUN apt-get -y -q install vim  
RUN apt-get -y -q install python-yaml  
RUN apt-get -y -q install python-ply  
RUN apt-get -y -q install sshpass  
RUN apt-get -y -q install python-pip  
RUN pip install IM-client  
COPY templates /ec3/templates  
ENV PATH="/ec3:${PATH}"  
CMD ["/bin/bash"]  

