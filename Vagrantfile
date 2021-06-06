# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
# vagrant up --provision - 
#
# in Vagrant Ruby script: plugins/synced_folders/smb/cap/mount_options.rb
# Edit: line 48
#       #def self.mount_name(machine, name, data)
#		def self.mount_name(machine, data)
# Due to bug: vagrant-2.2.15/plugins/synced_folders/smb/cap/mount_options.rb:48:in `mount_name': wrong number of arguments (given 2, expected 3) (ArgumentError)
# Original file in: https://github.com/hashicorp/vagrant/blob/main/plugins/synced_folders/smb/cap/mount_options.rb
# 
# Pre-req: (See https://github.com/hashicorp/vagrant/issues/11413) 
# New-Item -Path ENV: -Name "SMB_PASSWORD" -Value "****"  = Create ENV Var
# Set-Item -Path ENV: -Name "SMB_PASSWORD" -Value "****"  = Update ENV Var
#
# Up/Reload: 
# --provision - Force the provisioners to run.
# --provision-with x,y,z - This will only run the given provisioners. 
# For example, if you have a :shell and :chef_solo provisioner and run vagrant 
# reload --provision-with shell, only the shell provisioner will be run.

Vagrant.configure("2") do |config|

    config.vm.box = "hashicorp/bionic64"
	
	config.vm.synced_folder ".", "/vagrant", type: "smb", smb_username: "sspike", smb_password: ENV["SMB_PASSWORD"]

    config.vm.provider :vmware_esxi do |esxi|    
	
    #config.vm.network "public_network"
    #  REQUIRED!  ESXi hostname/IP
    esxi.esxi_hostname = '192.168.11.30'
    #  ESXi username
    esxi.esxi_username = 'root'
    esxi.esxi_password = 'file:.\.my_secret_file'
    esxi.esxi_virtual_network = ['VM Network']
    esxi.esxi_disk_store = 'DS1'
    esxi.guest_name = 'CorndelVm'
    esxi.guest_memsize = '2048'
    esxi.guest_numvcpus = '2'
    esxi.guest_snapshot_includememory = 'false'
    esxi.guest_virtualhw_version = '14'
    # TODO
    # Open a port (port forwarding?)
    # Set up environment variables (Use a shell provisioner?)


    # Install any dependencies
	# config.vm.provision "file", source: ".", destination: "/vagrant"

    # Run the server on `vagrant up` (Trigger?)
  end

	$script = <<-SCRIPT
	sudo apt-get update
	# Install pyenv prerequisites
	sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git libxml2-dev libxmlsec1-dev
	
	# pyenv install & setup
	#Step.1
	# git clone. Overwrite (keep up-to-date)
	echo "Installing pyenv"
	git clone https://github.com/pyenv/pyenv.git /home/vagrant/.pyenv-temp
	rsync -a /home/vagrant/.pyenv-temp/ /home/vagrant/.pyenv/
	rm -rf /home/vagrant/.pyenv-temp
	
	#Step.2 ### mutiple instances in $PATH ???
	###########################################
	echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
	echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
	
	#Step.3 ### mutiple instances in $PATH ???
	###########################################
	echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile
	exec "$SHELL"
	# Validation:
		# Check that pyenv is in your PATH: ~/which pyenv
		# Check that pyenv's shims directory is in PATH: echo $PATH | grep --color=auto "$(pyenv root)/shims"
		
	SCRIPT
	
    config.vm.provision "shell", privileged: false, inline: $script
	config.vm.network "forwarded_port", guest: 5000, host: 5000
	config.trigger.after :up, :reload do |trigger|
		trigger.name = "Launching App"
		trigger.info = "Running the TODO app setup script"
		trigger.run_remote = {privileged: false, inline: '
			# Install dependencies and launch
			pyenv install 3.9.0
			pyenv global 3.9.0
			
			#Step.4 ### Install poetry
			curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
			cd /vagrant
			poetry install
			nohup poetry run flask run --host=0.0.0.0 > ~/logs.txt 2>&1 &
			
		'}
	end

end












