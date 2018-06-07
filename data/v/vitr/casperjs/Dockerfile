# CasperJs  
# http://casperjs.org/  
#  
# Usage  
# exec mode  
# docker run --rm vitr/casperjs casperjs --version  
# docker run --rm vitr/casperjs phantomjs --version  
#  
# daemon mode  
# docker run -d --name casperjs-daemon -v /home/ubuntu/test:/mnt/test
--restart always vitr/casperjs  
FROM vitr/phantomjs  
  
MAINTAINER vitr https://vvitr.com  
  
RUN apt-get update -y && apt-get install -y \  
git \  
python \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
RUN git clone https://github.com/n1k0/casperjs.git  
RUN mv casperjs /opt/  
RUN ln -sf /opt/casperjs/bin/casperjs /usr/local/bin/casperjs  
RUN mkdir /home/casperjs-tests  
  
WORKDIR /home/casperjs-tests  
  
#optional  
#RUN apt-get purge git -y \  
# && apt-get autoremove -y  
# reset from parent image  
ENTRYPOINT []  
  
# run the image as daemon  
CMD echo "casperjs running..." && tail -f /dev/null  
  

