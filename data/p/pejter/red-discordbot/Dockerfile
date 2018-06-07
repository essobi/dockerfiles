FROM python:slim  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gcc \  
git \  
libav-tools \  
libffi-dev \  
libopus-dev \  
libssl-dev \  
make \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone -b develop --single-branch https://github.com/Cog-Creators/Red-
DiscordBot.git /app  
  
RUN pip install --no-cache-dir -r /app/requirements.txt  
  
VOLUME ["/app/data", "/app/cogs"]  
WORKDIR /app  
  
COPY run.py /scripts/  
  
CMD ["python", "/scripts/run.py"]  

