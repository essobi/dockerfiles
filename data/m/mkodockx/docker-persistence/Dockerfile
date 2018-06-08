FROM l3iggs/archlinux  
MAINTAINER Markus Kosmal <code@m-ko-x.de>  
  
RUN pacman -Sy  
RUN pacman -S --noconfirm --needed python-pip  
RUN pip install docker-py texttable  
  
ADD data/dig.py /dig.py  
WORKDIR /  
  
ENTRYPOINT ["python", "/dig.py" ]

