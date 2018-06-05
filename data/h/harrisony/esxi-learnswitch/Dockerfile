FROM python:2  
ENV PYVPX "VMware-pyVpx-6.5.0-4602587.zip"  
ENV vc_user="Administrator@vsphere.local" vc_password="VMware1!"
dvpg_name_list="DVPG-Nested-ESXi-Workload-1, DVPG-Nested-ESXi-Workload-2"  
RUN apt-get update && apt-get install -y --no-install-recommends unzip && rm
-rf /var/lib/apt/lists/*  
RUN pip install PyYAML six  
ADD VMware-pyVpx-6.5.0-4602587.zip /pyVpx.zip  
RUN ["unzip", "pyVpx.zip"]  
ADD learnswitch_cfg.py /pyVpx/  
ENTRYPOINT python /pyVpx/learnswitch_cfg.py  

