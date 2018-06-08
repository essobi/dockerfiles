FROM tsutomu7/scientific-python  
  
ADD nim.tgz /root/  
ENV PATH=/opt/Nim/bin:$PATH  
EXPOSE 8888  
WORKDIR /root  
RUN apt-get update --fix-missing && \  
apt-get install -y gcc git && \  
apt-get clean && \  
cd /opt && \  
git clone -b master git://github.com/nim-lang/Nim.git && \  
cd Nim && \  
git clone -b master --depth 1 git://github.com/nim-lang/csources && \  
cd csources && sh build.sh && \  
cd .. && bin/nim c koch && \  
./koch boot -d:release && \  
echo 'export PATH=/opt/Nim/bin:$PATH' >> /root/.bashrc && \  
mkdir -p /root/.local/share/jupyter/kernels/nim/ && \  
mv /root/kernel.json /root/.local/share/jupyter/kernels/nim/ && \  
mv /root/nimkernel.py /opt/conda/lib/python3.5/site-packages/ && \  
rm -rf /var/lib/apt/lists/*  
CMD ["sh", "-c", "jupyter notebook --ip=*"]  

