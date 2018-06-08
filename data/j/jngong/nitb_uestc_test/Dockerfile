FROM daocloud.io/jngong/matlab_v90_fsl_ubuntu  
MAINTAINER Jinnan Gong <gongjinnan1989@gmail.com>  
RUN apt-get -y install git  
RUN mkdir -p /script  
RUN cd /script && git clone https://github.com/gongjinnan/NITB_uestc_test  
RUN chmod 777 -R /script/NITB_uestc_test/  
ENV PATH=$PATH:/script/NITB_uestc_test/  

