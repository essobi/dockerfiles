FROM meyskens/desktop-base  
  
RUN apt-get update && apt-get install -y libpango1.0-0  
  
RUN wget -O bitscope.deb http://bitscope.com/download/files/bitscope-
dso_2.8.FE22H_amd64.deb &&\  
dpkg -i bitscope.deb &&\  
rm -f bitscope.deb  
  
CMD bitscope-dso

