FROM python  
RUN pip install urllib3 requests pandas tinys3  
WORKDIR /src  
RUN git clone
https://github.com/nehalbhanushali/Data_Wrangling_Edgar_Datasets.git /src  
CMD ["python", "/src/Part2_EDGAR_LogDataset.py"]  
  

