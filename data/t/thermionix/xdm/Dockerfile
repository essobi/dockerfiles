FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -y git python  
RUN git clone https://github.com/lad1337/XDM.git /usr/share/xdm  
  
#VOLUME /usr/share/xdm  
EXPOSE 8085  
CMD cd /usr/share/xdm ; python XDM.py --nolaunch  
  
#WORKDIR /usr/share/xdm  
#ENTRYPOINT ["python", "XDM.py", "--nolaunch"]  

