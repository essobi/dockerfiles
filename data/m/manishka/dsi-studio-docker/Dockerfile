FROM gcc:4.9  
RUN apt-get update && apt-get install -y qt5-qmake qt5-default git libboost-
all-dev \  
zlib1g zlib1g-dev libqt5opengl5-dev unzip libgl1-mesa-dev libglu1-mesa-dev
freeglut3-dev mesa-utils  
  
RUN mkdir dsistudio  
WORKDIR dsistudio  
RUN git clone -b master https://github.com/frankyeh/DSI-Studio.git src  
RUN wget https://github.com/frankyeh/TIPL/zipball/master  
RUN unzip master  
RUN mv frankyeh-TIPL-* image  
RUN mv image src  
  
RUN mkdir build  
WORKDIR build  
RUN qmake ../src && make  
  
WORKDIR ..  
RUN wget https://www.dropbox.com/s/ew3rv0jrqqny2dq/dsi_studio_64.zip?dl=1  
RUN mv dsi_studio_64.zip?dl=1 dsi_studio_64.zip  
RUN unzip dsi_studio_64.zip  
WORKDIR dsi_studio_64  
RUN find . -name '*.dll' -exec rm {} \;  
RUN rmdir iconengines imageformats platforms printsupport  
RUN rm dsi_studio.exe  
RUN cp ../build/dsi_studio .  
  
CMD ./dsi_studio  

