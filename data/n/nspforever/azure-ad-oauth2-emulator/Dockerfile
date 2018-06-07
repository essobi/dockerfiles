FROM ubuntu:14.04  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:fkrull/deadsnakes \  
&& apt-get update \  
&& apt-get install -y \  
python3.5 \  
python3-pip \  
python3-setuptools \  
build-essential \  
libffi-dev \  
libssl-dev \  
nginx \  
python-setuptools  
  
RUN easy_install supervisor  
RUN easy_install supervisor-stdout  
RUN pip3 install uwsgi  
  
RUN rm -rf /etc/nginx/sites-enabled/default && echo "daemon off;" >>
/etc/nginx/nginx.conf  
RUN ln -s /AzureADOAuthEmulator/conf/emulator_nginx.conf /etc/nginx/sites-
enabled/emulator_nginx.conf  
RUN ln -s /AzureADOAuthEmulator/conf/supervisord.conf /etc/supervisord.conf  
  
COPY requirements.txt .  
RUN pip3 install -r requirements.txt  
  
EXPOSE 8080  
WORKDIR /AzureADOAuthEmulator  
COPY . /AzureADOAuthEmulator  
RUN chmod 775 /AzureADOAuthEmulator/start_emulator.sh  
  
CMD ["/bin/bash", "/AzureADOAuthEmulator/start_emulator.sh"]  
  

