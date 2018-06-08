FROM ubuntu  
  
MAINTAINER Johannes <johannes@number13.de>  
  
RUN apt-get update && apt-get install -y \  
python3 \  
python3-dev \  
python3-pip \  
git  
  
RUN git clone https://github.com/number13dev/mincloud.git  
  
WORKDIR /mincloud  
RUN pip3 install -r requirements.txt  
RUN chmod +x run.sh  
  
EXPOSE 80  
CMD ["/mincloud/run.sh"]  

