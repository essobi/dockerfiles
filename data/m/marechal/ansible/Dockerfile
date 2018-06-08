FROM fedora  
RUN dnf -y update  
RUN dnf -y install sudo which python python-pip krb5-workstation python-devel
krb5-devel krb5-libs gcc  
RUN pip install ansible  
RUN pip install pywinrm  
RUN pip install pywinrm[kerberos]  
RUN pip install PyVmomi  

