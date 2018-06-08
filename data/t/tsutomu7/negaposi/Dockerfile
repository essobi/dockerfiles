FROM tsutomu7/janome  
  
ADD http://www.cl.ecei.tohoku.ac.jp/resources/sent_lex/wago.121808.pn /root/  
ADD http://www.cl.ecei.tohoku.ac.jp/resources/sent_lex/pn.csv.m3.120408.trim
/root/  
COPY run.py /root/  
WORKDIR /root/  
ENTRYPOINT ["python3", "run.py"]  

