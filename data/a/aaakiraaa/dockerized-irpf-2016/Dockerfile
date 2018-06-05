FROM ubuntu:14.04  
RUN echo "#!/usr/bin/env bash" > /bin/irpf-2016; \  
echo "[ ! -d /usr/local/IRPF2016/ ] && ./IRPF2016Linux-x86_64v1.1.bin &&
./Receitanet-1.07-x64.bin" >> /bin/irpf-2016; \  
echo "/usr/bin/java -Xms128M -Xmx512M -jar /usr/local/IRPF2016/irpf.jar" >>
/bin/irpf-2016; \  
chmod u+x /bin/irpf-2016; \  
apt-get update; \  
apt-get install -y openjdk-7-jdk; \  
apt-get install -y wget  
RUN wget
http://downloadirpf.receita.fazenda.gov.br/irpf/2016/IRPF2016Linux-x86_64v1.1.bin;
\  
chmod u+x IRPF2016Linux-x86_64v1.1.bin; \  
wget
http://www.receita.fazenda.gov.br/publico/programas/receitanet/Receitanet-1.07-x64.bin;
\  
chmod u+x Receitanet-1.07-x64.bin; \  
mkdir /root/shared  
  

