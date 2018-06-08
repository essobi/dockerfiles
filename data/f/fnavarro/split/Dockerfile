FROM debian  
  
RUN apt-get update  
  
RUN apt-get install -y \  
samtools=1.3.1-3 \  
python-pip \  
wget  
  
RUN pip install python-Levenshtein numpy scipy  
  
RUN mkdir -p /src; \  
cd /src; \  
wget
"https://raw.githubusercontent.com/fabiocpn/pd_2017_splitreads/master/scour.py"
-O scour.py  
  
RUN mkdir -p /src; \  
cd /src; \  
wget
"https://raw.githubusercontent.com/fabiocpn/pd_2017_splitreads/master/split.sh"
-O split.sh; \  
chmod +x /src/split.sh  
  

