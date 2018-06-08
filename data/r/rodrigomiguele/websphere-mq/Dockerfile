FROM ubuntu  
  
RUN apt-get update && \  
apt-get install -y curl rpm rpm2cpio pax && \  
mkdir $HOME/webspheremq && \  
cd $HOME/webspheremq && \  
curl -O
http://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqadv/mqadv_dev75_linux_x86-64.tar.gz
&& \  
tar -xvf mqadv_dev75_linux_x86-64.tar.gz && \  
./mqlicense.sh -accept -text_only && \  
./crtmqpkg wmq && \  
cd /var/tmp/mq_rpms/wmq/x86_64 && \  
rpm -ivh --nodeps --force-debian --prefix /opt/mqm MQSeriesRuntime*rpm
MQSeriesServer*rpm MQSeriesSDK*rpm MQSeriesClient*rpm MQSeriesJava*rpm
MQSeriesSamples*rpm MQSeriesGSKit*rpm MQSeriesMan*rpm && \  
rm -rf $HOME/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /usr/lib64 && \  
/opt/mqm/bin/setmqinst -i -p /opt/mqm  
  
USER mqm  
  
CMD dspmqver  

