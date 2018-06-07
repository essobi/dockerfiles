# base image  
FROM himnark/idoodi-ocr-engine-dependencies  
  
# Copy application source code to SRCDIR  
#COPY $DOCKYARD_SRC $DOCKYARD_OPT  
# Create himnark directory  
RUN cd $ROOT_DIR && mkdir himnark && cd himnark && mkdir res && mkdir src  
  
# Copy application source code to SRCDIR  
COPY CMakeLists.txt $ROOT_DIR/himnark  
COPY res $ROOT_DIR/himnark/res  
COPY src $ROOT_DIR/himnark/src  
  
#build himnark  
RUN cd $ROOT_DIR/himnark && mkdir build && cd build && cmake ../ && make  

