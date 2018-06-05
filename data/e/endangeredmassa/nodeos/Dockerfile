FROM nodeos/base  
  
ENV HOME /root  
ENV PATH /root/bin:/usr/bin:/usr/sbin:/bin:/sbin  
  
ENTRYPOINT ["init"]  
  
MAINTAINER Sean Massa <endangeredmassa@gmail.com>  
  
RUN npkg install bin-nsh  
RUN npkg install bin-man  
RUN npkg install bin-fs  
RUN npkg install bin-pwd  
RUN npkg install bin-ifconfig  
  
RUN npkg install hipster@0.15.3  
RUN npkg install boxes  
  
CMD ["nsh"]

