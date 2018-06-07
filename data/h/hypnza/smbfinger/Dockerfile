# Taken from "Responder", a network take-over set of tools created and
maintained  
# by Laurent Gaffie. See https://github.com/lgandx/Responder  
FROM elyase/staticpython:latest  
  
WORKDIR /Responder  
  
ADD files/odict.py /Responder  
ADD files/RunFinger.py /Responder  
  
ENTRYPOINT ["python","RunFinger.py","-i"]  
CMD ["localhost"]  

