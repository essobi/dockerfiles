FROM ubuntu  
  
RUN apt-get update && apt-get install -y python libboost-regex-dev libboost-
program-options-dev libboost-system-dev libboost-filesystem-dev libssl-dev
build-essential cmake git  
RUN git clone https://github.com/JusticeRage/Manalyze.git && cd Manalyze &&
cmake . && make  
RUN python /Manalyze/bin/yara_rules/update_clamav_signatures.py || true  

