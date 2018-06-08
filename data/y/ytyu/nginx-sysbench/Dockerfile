FROM nginx:latest  
RUN apt-get update \  
&& apt-get install -y sysbench \  
&& rm -rfv /var/lib/apt/lists/*  
  
COPY stream /root/  
COPY sysbench.sh /root/  
RUN chmod 700 /root/sysbench.sh \  
&& chmod 700 /root/stream  
CMD sh /root/sysbench.sh  

