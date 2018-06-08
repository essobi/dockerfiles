# Copyright 2015 SIGMA INFORMATIQUE, Société par actions simplifiée au capital
de 1 649 600 Euros  
# 8 Rue Newton – CS84533 - 44245 LA CHAPELLE-SUR-ERDRE CEDEX – FRANCE  
# Tel : +33 (0) 2 40 37 14 00 – Fax : +33 (0) 2 40 37 72 20 – www.sigma.fr  
# 872 803 390 R.C.S. NANTES – APE : 6202B – TVA : FR39 872 803 390  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
#
=============================================================================  
#  
# Build:  
# docker build -t sigmainformatique/dloc .  
# Run:  
# docker run -it -v <your directory>:/code sigmainformatique/dloc  
#  
FROM google/dart  
MAINTAINER Sigma Informatique Team <github@sigma.fr>  
  
ENV PATH $PATH:/root/.pub-cache/bin  
RUN pub global activate dloc  
  
VOLUME ["/code"]  
WORKDIR /code  
  
CMD []  
ENTRYPOINT ["dloc"]  

