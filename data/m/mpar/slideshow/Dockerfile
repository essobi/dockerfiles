from jenserat/seafile  
RUN apt-get update && apt-get install -y libtiff5-dev libjpeg-turbo8-dev
zlib1g-dev \  
libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk \  
libexempi-dev libexempi3 python-pip  
WORKDIR /opt  
ADD requirements.txt /opt/requirements.txt  
RUN pip install -r /opt/requirements.txt  
ADD src/ /opt/app  
RUN mkdir /etc/service/seafuse /etc/service/screensaver  
ADD seafile-fuse.sh /etc/service/seafuse/run  
ADD screensaver.sh /etc/service/screensaver/run

