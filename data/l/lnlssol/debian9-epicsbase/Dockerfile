FROM debian:stretch  
# Install Epics  
RUN apt-get update && apt-get install git libreadline7 libreadline-dev
libtinfo-dev readline-common -y  
RUN git clone https://github.com/lnls-sol/epics-base_debs  
# ignore epics-perl (this package have some problems)  
RUN rm epics-base_debs/debs/epics-perl_3.15.3-13_amd64.deb  
RUN dpkg -i epics-base_debs/debs/*.deb  
RUN rm -rf epics-base_debs  
RUN mkdir /usr/local/epics  
RUN ln -s /usr/lib/epics /usr/local/epics/base  
CMD bash  

