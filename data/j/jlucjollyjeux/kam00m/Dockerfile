FROM python  
MAINTAINER Jeanluc Jollyjeux <jlucjollyjeux@gmail.com>  
COPY voila.py /src/voila.py  
  
RUN pip install git+https://github.com/pwaller/pyfiglet  
RUN pip install termcolor  
RUN pip install colorama  
  
ENTRYPOINT [ "python", "./src/voila.py"]  

