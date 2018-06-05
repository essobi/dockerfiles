FROM vpanov/openwrt-cc-mvebu  
ADD deps /opt/SDK/package  
RUN \  
ln -s /opt/SDK /opt/openwrt && \  
make -C /opt/SDK package/boost/compile && \  
make -C /opt/SDK package/curl/compile && \  
make -C /opt/SDK package/gtest/compile && \  
make -C /opt/SDK package/libuv/compile && \  
rm -rf \  
/opt/SDK/build_dir \  
/opt/SDK/package/boost \  
/opt/SDK/package/curl \  
/opt/SDK/package/gtest \  
/opt/SDK/package/libuv \  
&& \  
mv /opt/SDK/bin/mvebu/packages/base /opt/SDK/bin/mvebu/packages/sdk && \  
sleep 2 && \  
touch /opt/SDK/timestamp && \  
echo OK!  

