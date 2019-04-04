Bootstrap: docker
From: continuumio/miniconda3
%files
./* ./

%post
# install packages.
/opt/conda/bin/conda env create -f /enviroment.yml

#Activate the enviroment
. /opt/conda/bin/activate main

%runscript
ls -l
exec python /src/seedcoatmap.py "$@"
