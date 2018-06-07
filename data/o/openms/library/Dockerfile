FROM openms/contrib  
  
WORKDIR /  
RUN git clone \--depth 1 https://github.com/OpenMS/OpenMS.git -b nightly  
RUN mkdir openms-build  
  
WORKDIR /openms-build  
  
RUN cmake -DOPENMS_CONTRIB_LIBS="/contrib-build"
-DCMAKE_PREFIX_PATH="/usr;/usr/local" -DBOOST_USE_STATIC=OFF ../OpenMS  
RUN make OpenMS  

