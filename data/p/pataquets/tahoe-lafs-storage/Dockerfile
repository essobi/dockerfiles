FROM pataquets/tahoe-lafs-node  
  
RUN \  
sed -i \  
-e 's/nickname = /nickname = tahoe-lafs-storage/' \  
.tahoe/tahoe.cfg \  
&& \  
nl .tahoe/tahoe.cfg  

