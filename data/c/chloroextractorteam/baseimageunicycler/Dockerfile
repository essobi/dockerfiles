FROM chloroextractorteam/baseimage  
  
LABEL maintainer="foersterfrank@gmx.de"  
  
WORKDIR /opt  
  
RUN apt update && apt install --yes --no-install-recommends \  
mummer \  
python-numpy \  
python-matplotlib \  
time && \  
git clone --branch 0.5.0 https://github.com/isovic/racon.git racon && \  
cd racon && \  
make modules && \  
make tools && \  
make && \  
find -type d -name ".git" | xargs rm -rf && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH=/opt/racon/bin/:"$PATH"  
  
RUN mkdir pilon-1.22 && \  
cd pilon-1.22 && \  
wget
https://github.com/broadinstitute/pilon/releases/download/v1.22/pilon-1.22.jar
&& \  
ln -s pilon-1.22.jar pilon.jar && \  
bash -c 'echo -e "#!/bin/bash\njava -Xmx2G -jar /opt/pilon-1.22/pilon.jar $@"
> pilon' && \  
chmod +x pilon  
ENV PATH=/opt/pilon-1.22/:"$PATH"  
  
ENV PYTHONPATH=/opt/lib/python3.5/site-packages/  
ENV PATH=/opt/bin/:"$PATH"  
RUN git clone --branch v0.4.4 https://github.com/rrwick/Unicycler.git
/opt/unicycler && \  
cd /opt/unicycler && \  
rm -rf .git && \  
sed -i 's/str(min(8, multiprocessing.cpu_count/str(min(1,
multiprocessing.cpu_count/' setup.py && \  
python3 setup.py install --prefix=/opt/  
  

