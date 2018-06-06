FROM zasdfgbnmsystem/basic  
USER user  
RUN yaourt -Syua --noconfirm  
RUN yaourt -S --noconfirm python-rdkit-git || true  
USER root  
RUN pip install ase || true  
RUN pip install asap3 || true  

