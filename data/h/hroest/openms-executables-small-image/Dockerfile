FROM hroest/openms_dependencies:v2.2.0-small  
  
WORKDIR /  
  
RUN mkdir openms-build  
RUN git clone https://github.com/OpenMS/OpenMS.git && \  
cd openms-build && \  
cmake -DCMAKE_PREFIX_PATH="/contrib-build/;/usr/;/usr/local"
-DBOOST_USE_STATIC=OFF ../OpenMS && \  
make TOPP && make UTILS && \  
rm -rf src doc CMakeFiles && \  
rm -rf /OpenMS/.git/ /OpenMS/src /OpenMS/doc /OpenMS/tools
/OpenMS/share/OpenMS/examples/  
  
WORKDIR /  
ENV PATH="/openms-build/bin/:${PATH}"  

