FROM alpine:3.1  
# Update  
RUN apk add --update python py-pip  
  
# Install app dependencies  
RUN pip install requests  
  
# COPY files  
COPY DonationLib.py /src/DonationLib.py  
COPY __init__.py /src/__init__.py  
COPY donation.py /src/donation.py  
COPY setup.py /src/setup.py  
COPY variables.py /src/variables.py  
  
CMD ["python", "/src/donation.py"]  

