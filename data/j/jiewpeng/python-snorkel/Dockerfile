FROM ubuntu:17.04  
RUN \  
wget https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh &&\  
chmod +x Anaconda2-5.0.1-Linux-x86_64.sh &&\  
./Anaconda2-5.0.1-Linux-x86_64.sh &&\  
rm Anaconda2-5.0.1-Linux-x86_64.sh &&\  
export PATH=~/anaconda/bin:"$PATH" &&\  
echo '\n\nexport PATH=~/anaconda/bin:"$PATH"' >> .bashrc &&\  
git clone https://github.com/HazyResearch/snorkel.git &&\  
cd snorkel &&\  
pip install --requirement python-package-requirement.txt &&\  
jupyter nbextension enable \--py widgetsnbextension --sys-prefix  
  
CMD ['./run.sh']

