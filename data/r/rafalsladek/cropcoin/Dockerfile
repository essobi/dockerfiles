FROM rafalsladek/bitcoin-docker-base:latest  
  
ENV TMP_FOLDER "/usr/local/src/"  
ENV BINARY_FILE "/usr/local/bin/cropcoind"  
ENV CROP_REPO "https://github.com/Cropdev/CropDev.git"  
ENV RED '\033[0;31m'  
ENV GREEN '\033[0;32m'  
ENV NC '\033[0m'  
RUN git clone $CROP_REPO $TMP_FOLDER && \  
cd $TMP_FOLDER/src/secp256k1 && \  
ls -al && \  
chmod +x autogen.sh && \  
./autogen.sh && \  
./configure --enable-module-recovery && \  
make && \  
./tests && \  
cd .. && \  
mkdir obj/support && \  
mkdir obj/crypto && \  
make -f makefile.unix && \  
cp -a cropcoind $BINARY_FILE  

