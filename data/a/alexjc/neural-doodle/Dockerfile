FROM ubuntu:14.04  
# Install dependencies  
RUN apt-get -qq update && \  
apt-get -qq install --assume-yes \  
"build-essential" \  
"git" \  
"wget" \  
"pkg-config" && \  
rm -rf /var/lib/apt/lists/*  
  
# Miniconda.  
RUN wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.0.5-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
# Install requirements before copying project files  
WORKDIR /nd  
COPY requirements.txt .  
RUN /opt/conda/bin/conda install -q -y conda numpy llvmlite numba pip scikit-
learn pillow  
RUN /opt/conda/bin/python3 -m pip install -q -r "requirements.txt"  
  
# Copy only required project files  
COPY doodle.py .  
  
# Get a pre-trained neural network, non-commercial & attribution. (GELU2)  
RUN wget -q "https://github.com/alexjc/neural-
doodle/releases/download/v0.0/geln3_conv.pkl"  
  
# Set an entrypoint to the main doodle.py script  
ENTRYPOINT ["/opt/conda/bin/python3", "doodle.py", "--device=cpu"]  

