FROM python:3.6  
MAINTAINER Fumihiro Kato <fumi@fumi.me>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y vim-nox locales  
  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  
RUN echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen  
RUN locale-gen  
ENV LANG en_US.UTF-8  
RUN mkdir -p /dld/logs /dld-wd  
  
WORKDIR /dld-wd/  
  
COPY requirements.txt config.py dld.py tools.py /dld/  
  
COPY baselibs/ /dld/baselibs/  
  
COPY data/ /dld/data/  
  
RUN pip3 install --no-cache-dir -r /dld/requirements.txt  
  
ENTRYPOINT ["python", "/dld/dld.py"]  
  
CMD ["--help"]  

