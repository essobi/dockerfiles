FROM tagplus5/wine  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
sudo apt-get update && \  
sudo apt-get upgrade -y && \  
sudo apt-get install -y \--no-install-recommends wget unzip && \  
mkdir -p /home/ubuntu/heidisql && \  
cd /home/ubuntu/heidisql && \  
wget http://www.heidisql.com/downloads/releases/HeidiSQL_9.4_Portable.zip && \  
unzip /home/ubuntu/heidisql/HeidiSQL_9.4_Portable.zip && \  
rm /home/ubuntu/heidisql/HeidiSQL_9.4_Portable.zip && \  
wget -q --output-document=heidisql_latest.exe http://www.heidisql.com$(wget -q
-O - http://www.heidisql.com/download.php | grep -oh
/builds/heidisql32.r[0-9]*.exe | head -1) && \  
sudo apt-get autoremove -y && \  
sudo rm -rf /var/lib/apt/lists/*  
  
CMD ["wine", "/home/ubuntu/heidisql/heidisql.exe"]  

