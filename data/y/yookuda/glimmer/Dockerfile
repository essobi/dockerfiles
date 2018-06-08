FROM ubuntu:14.04  
MAINTAINER yookuda <yookuda@nig.ac.jp>  
WORKDIR /tmp  
RUN apt-get update && \  
apt-get -y install wget make g++ csh && \  
apt-get clean  
RUN wget https://ccb.jhu.edu/software/glimmer/glimmer302b.tar.gz && \  
tar xzvf glimmer302b.tar.gz && \  
cd glimmer3.02/src && \  
make && \  
mv /tmp/glimmer3.02 /opt/ && \  
ln -s /opt/glimmer3.02 /opt/glimmer && \  
rm -rf /tmp/*  
RUN wget ftp://ftp.cbcb.umd.edu/pub/software/elph/ELPH-1.0.1.tar.gz && \  
tar xzvf ELPH-1.0.1.tar.gz && \  
cd ELPH/sources && \  
make && \  
cp elph /usr/local/bin/ && \  
rm -rf /tmp/*  
RUN cd /opt/glimmer/scripts/ && \  
sed -i -e '28,29d' g3-from-scratch.csh && \  
sed -i '28i set awkpath = /opt/glimmer/scripts' g3-from-scratch.csh && \  
sed -i '29i set glimmerpath = /opt/glimmer/bin' g3-from-scratch.csh && \  
sed -i -e '30,32d' g3-from-training.csh && \  
sed -i '30i set awkpath = /opt/glimmer/scripts' g3-from-training.csh && \  
sed -i '31i set glimmerpath = /opt/glimmer/bin' g3-from-training.csh && \  
sed -i '32i set elphbin = /usr/local/bin/elph' g3-from-training.csh && \  
sed -i -e '34,36d' g3-iterated.csh && \  
sed -i '34i set awkpath = /opt/glimmer/scripts' g3-iterated.csh && \  
sed -i '35i set glimmerpath = /opt/glimmer/bin' g3-iterated.csh && \  
sed -i '36i set elphbin = /usr/local/bin/elph' g3-iterated.csh && \  
sed -i -e '1d' *.awk && \  
sed -i '1i #!/usr/bin/awk -f' *.awk  
ENV PATH
/opt/glimmer/bin:/opt/glimmer/scripts:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN mkdir /data  

