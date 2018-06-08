FROM radial/busyboxplus  
  
RUN \  
mkdir -p /vmx/models/569a262df94ae8aaab2dd866e7abb8b893c7 && \  
cd /vmx/models/569a262df94ae8aaab2dd866e7abb8b893c7 && \  
curl
https://models.vision.ai/models/569a262df94ae8aaab2dd866e7abb8b893c7/image.jpg
-o image.jpg && \  
curl
https://models.vision.ai/models/569a262df94ae8aaab2dd866e7abb8b893c7/compiled.data
-o compiled.data && \  
curl
https://models.vision.ai/models/569a262df94ae8aaab2dd866e7abb8b893c7/model.json
-o model.json && \  
ln -s compiled.data model.data  
  
VOLUME /vmx/models  

