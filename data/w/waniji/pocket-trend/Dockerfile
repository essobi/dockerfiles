FROM kazeburo/perl:v5.18  
RUN apt-get -y update  
RUN apt-get -y install libssl-dev  
RUN cpanm -n Carton  
RUN cd /opt; git clone https://github.com/waniji/PocketTrend.git  
RUN cd /opt/PocketTrend; carton install  
WORKDIR /opt/PocketTrend  
EXPOSE 5000  
CMD ["carton","exec","--","perl","-Ilib","script/pockettrend-server","--
host","0"]  

