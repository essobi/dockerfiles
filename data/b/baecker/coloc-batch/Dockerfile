FROM baecker/fiji-base:latest  
  
RUN cd plugins && wget -O jacop_.jar
http://imagejdocu.tudor.lu/lib/exe/fetch.php?media=plugin:analysis:jacop_2.0:just_another_colocalization_plugin:jacop_.jar  
  
RUN cd /fiji/macros && wget -O coloc.ijm
https://gist.githubusercontent.com/volker-
baecker/6de91df9af79fd252436e8016f282adb/raw/92cc251927f6e76011f9ebfbeb2f8af3844bf489/coloc.ijm  
RUN cd /fiji && wget -O run-coloc.sh
https://gist.githubusercontent.com/volker-
baecker/42e720f3174b52b583f32299867d4c6b/raw/57a843e81086e6313e865786cc94de91993a4d32/run-
coloc.sh && chmod a+x run-coloc.sh  
  
RUN cd /fiji/macros && wget -O metrics.ijm
https://gist.githubusercontent.com/volker-
baecker/f298621247e62011ba3913d70af9ffed/raw/0a9803e955ba3adfae608adf78b09de1e1f540c3/metrics.ijm  
RUN cd /fiji && wget -O run-metrics.sh
https://gist.githubusercontent.com/volker-
baecker/1a273b28c62d010ab5c266d71b89ba64/raw/52ec60fd96cc5654f35f54987087ac08bac5ba82/run-
metrics.sh && chmod a+x run-metrics.sh  

