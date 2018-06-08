FROM python  
RUN pip install --upgrade pip  
RUN pip install pydicom  
RUN pip install Image  
RUN pip install sets  
RUN pip install cm  
RUN pip install scipy  
RUN pip install numpy  
RUN pip install setuptools  
RUN pip install -U scikit-image  
RUN apt-get update --fix-missing && apt-get install -y --fix-missing r-base  
COPY train.py /train.py  
COPY train.py /modelState/train.py  
COPY train.sh /train.sh  
COPY score_sc1.sh /score_sc1.sh  
RUN touch blue_training  
RUN /train.sh  

