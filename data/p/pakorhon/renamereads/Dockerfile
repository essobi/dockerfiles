FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y python git  
WORKDIR /root  
RUN git clone -b 'v1.0.4-beta' \--single-branch --depth 1
https://github.com/vetscience/Tools  
RUN cp Tools/Cwl/renamereads/base.py . && cp
Tools/Cwl/renamereads/renameFasta.py . && cp
Tools/Cwl/renamereads/renamereads.sh .  
RUN chmod uog+x renamereads.sh /root  
ENTRYPOINT ["/root/renamereads.sh"]  

