# Copyright (C) 2017 \- Universitat Pompeu Fabra  
# Author - Carlos Yagüe Méndez <carlos.yague@upf.edu>  
  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
  
  
FROM ubuntu:16.10  
  
MAINTAINER Carlos Yagüe Méndez <carlos.yague@upf.edu>  
  
################################## APT-GET
#####################################  
RUN apt-get -qq update && apt-get -qq install -y \  
python3-setuptools \  
python3 \  
python3-pip \  
python3-numpy \  
python3-scipy \  
python3-matplotlib \  
python3-pillow \  
git \  
wget  
# && rm -rf /var/lib/apt/lists/*  
  
# 731MB  
  
# RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends \  
  
RUN pip3 install --no-cache-dir PyWavelets  
  
RUN wget
https://raw.githubusercontent.com/carlosym/rkt_dicom_ecg_peaks_detection/master/rkt_dicom_ecg_pics_detection.py  
RUN mv rkt_dicom_ecg_pics_detection.py /home/rkt_dicom_ecg_pics_detection.py  
  
RUN groupadd -r host && useradd -r -g host host && usermod -u 1000 host  
USER host  
  
WORKDIR "/home"  
  
ENTRYPOINT ["python3", "/home/rkt_dicom_ecg_pics_detection.py"]  
  
  
  
  

