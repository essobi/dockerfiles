FROM perfectweb/base:cuda-8.0-devel-ubuntu16.04-v1  
MAINTAINER Alin Jurj <office@perfectweb.ro>  
  
ADD https://github.com/nanopool/Claymore-Dual-
Miner/releases/download/v9.8/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.v9.8.-.LINUX.tar.gz
/  
RUN mkdir /claymore  
RUN tar xvf
Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.v9.8.-.LINUX.tar.gz
-C /claymore  
RUN rm -rf /claymore/*.txt  
  
ENTRYPOINT ["/claymore/ethdcrminer64"]  
CMD ["-epool", "closest.eth.perfectmine.io:8008", "-ewal",
"0x717006Bf6B17cf8e1835a0c4dEC22D25D8972795", "-epsw", "x", "-allpools", "1",
"-allcoins", "1", "-dpsw", "x", "-dwal",
"480b19a1fee9a1c0579cc4438c5fd54785994f2fea989141d2aa99dc172ff52dcb55c44ea88d/dual",
"-dpool", "stratum+tcp://sia-eu1.nanopool.org:7777", "-dcoin", "sia",
"-eworker", "dual", "-dbg", "-1", "-tt", "1", "-ttdcr", "80", "-tstop", "95",
"-etha", "2"]  

