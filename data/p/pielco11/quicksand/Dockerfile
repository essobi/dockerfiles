FROM python:2.7.14  
FROM ubuntu:16.04  
LABEL maintainer "https://github.com/pielco11"  
LABEL malice.plugin.repository =
"https://github.com/pielco11/quicksand_lite.git"  
LABEL malice.plugin.category="av"  
LABEL malice.plugin.mime="*"  
LABEL malice.plugin.docker.engine="*"  
  
WORKDIR /mal  
  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get install -y zlib1g-dev libzip-dev \  
build-essential git libzip-dev libyara-dev python-pip  
RUN git clone \--depth 1 https://github.com/pielco11/quicksand_lite.git  
RUN cd quicksand_lite && ./build.sh && cp quicksand_exe.yara
quicksand_exploits.yara quicksand_general.yara quicksand.out handler.py /mal  
  
RUN pip install elasticsearch  
  
CMD []  
  
ENTRYPOINT ["python", "/mal/handler.py", "-jmnr"]  
  

