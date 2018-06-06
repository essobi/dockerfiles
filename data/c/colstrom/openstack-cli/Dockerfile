FROM colstrom/python  
  
RUN pip install python-openstackclient \  
&& sed -i 's/subprocess.mswindows/subprocess._mswindows/g'
/usr/local/lib/python3.5/dist-packages/cmd2.py  
  
ENTRYPOINT ["/usr/local/bin/openstack"]  

