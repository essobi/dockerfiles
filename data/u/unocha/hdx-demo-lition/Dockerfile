FROM unocha/alpine-base-python3:latest  
  
MAINTAINER "Serban Teodorescu <teodorescu.serban@gmail.com>"  
ENV HDX_URL="http://demo.acme.local" \  
HDX_KEY="abcabcabcabcabc" \  
HDX_AGENT="alladin"  
COPY . /srv  
  
WORKDIR /srv  
  
RUN pip install -r requirements.txt  
  
ENTRYPOINT ["python3", "demo-lition.py"]  

