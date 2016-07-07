# pyramid_tutorial


#Set the profile
. setup_env

# Create and Activate Virtual Environment
pyvenv-3.5 --without-pip $VENV
source $VENV/bin/activate

#Fix CA Certificates
#http://askubuntu.com/questions/646594/how-to-fix-ca-cert-issues-with-curl-in-ubuntu-14-04

# Install pip and setup tools
curl https://bootstrap.pypa.io/get-pip.py | python

#Create $VENV/bin/activate_this.py with the content in https://github.com/jmcantrell/vim-virtualenv/issues/45

# Install Pyramid
pip install "pyramid==1.7"
