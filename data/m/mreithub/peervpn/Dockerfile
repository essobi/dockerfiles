FROM debian:jessie  
  
RUN apt-get update && apt-get install -y build-essential libssh-dev wget
python3  
RUN mkdir -p /tmp/build/  
WORKDIR /tmp/build/  
RUN wget https://peervpn.net/files/peervpn-0-044.tar.gz  
RUN tar xfz peervpn-*.tar.gz --strip-components=1  
  
RUN make clean all  
RUN mv peervpn /usr/local/bin/  
  
COPY run.py /  
COPY peervpn.conf.tpl /root/  
  
ENTRYPOINT [ "/run.py" ]  
CMD [ "/peervpn.conf" ]  

