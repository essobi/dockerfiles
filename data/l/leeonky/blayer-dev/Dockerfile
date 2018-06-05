FROM leeonky/ctest:ubuntu  
  
RUN sudo apt-get update && sudo apt-get install -y yasm && cd ~ && \  
wget https://gitee.com/leeonky/tools_dev/raw/master/ffmpeg-3.3.1.tar.bz2 && \  
tar xf ffmpeg-3.3.1.tar.bz2 && \  
cd ffmpeg-3.3.1 && \  
./configure --enable-shared && make -j8 && sudo make install && \  
cd .. && rm -rf ffmpeg-3.3.1*  
  
RUN sudo apt-get install -y libsdl2-dev libsdl2-ttf-dev portaudio19-dev  
RUN sudo apt-get install -y libcunit1-dev  
  
#RUN cd /tmp/ && wget
https://gitee.com/leeonky/tools_dev/raw/master/SDL2-2.0.5.tar.gz && \  
#tar -zxvf SDL2-2.0.5.tar.gz && \  
#cd SDL2-2.0.5 && \  
#./configure && \  
#make && \  
#sudo make install && \  
#cd .. && \  
#rm -rf SDL2-2.0.5*  
CMD bash  

