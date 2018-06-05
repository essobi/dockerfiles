FROM python  
RUN pip install urllib3 requests pandas tinys3  
WORKDIR /src  
RUN git clone https://89bcedda4545305eb4910f445d22976f76818767:x-oauth-
basic@github.com/vasantivmahajan/DataWrangling_AnomalyDetection_Tableau_Visualization_EDGAR_Log_Data.git
/src  
CMD ["python", "/src/Part2_EDGAR_LogDataset.py"]  
  

