FROM ubuntu  
  
# RUN wget -O- http://shadowsocks.org/debian/1D27208A.gpg | sudo apt-key add -  
COPY 1D27208A.gpg /tmp/  
RUN sudo apt-key add /tmp/1D27208A.gpg  
RUN echo "deb http://shadowsocks.org/debian wheezy main" >>
"/etc/apt/sources.list"  
RUN apt-get update && apt-get install -y shadowsocks-libev  
  
EXPOSE 8388  
ENTRYPOINT [ "ss-server", "-s", "0.0.0.0", "-t", "60" ]  
  
CMD [ "-p", "8388", "-k", "PASSWORD", "-m", "rc4" ]  

