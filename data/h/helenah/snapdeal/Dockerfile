FROM python:3.4.3-onbuild  
RUN pip3 install urllib3  
RUN pip3 install beautifulsoup4  
RUN pip3 install pymongo  
  
RUN mkdir /snapdealout  
RUN touch /snapdealout/testfile.txt  
RUN chmod -R 777 /snapdealout  
  
CMD [ "python3", "./snapdeal_csv_scrap_1.py",
"snapdeal_product_url_one_k.csv"]  

